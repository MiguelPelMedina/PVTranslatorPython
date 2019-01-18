'''
Created on 15 ene. 2019

@author: Alberto
'''
from datetime import datetime
import os
import webapp2
import jinja2
import populate as po
from google.appengine.api import search
from google.appengine.api import users

from google.auth import id_token
from google.auth.transport import requests

from google.appengine.ext import db
from models import Modulo, Campanya, Usuario, Comentario 

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))

class Inicio (BaseHandler):        
    def get(self):
        #ESTO LLAMA A populate.py PARA LLENAR LOS DATOS DE LA BD
        po.Populate().addData()
        self.render_template('index.html', {})
    
    
class ListaModulos(BaseHandler):
    

    def get(self):
        listaModulos = Modulo.all()
        usuarios = Usuario.all()
        self.render_template('listaModulos.html', {'listaModulos': listaModulos, 'listaUsuarios':usuarios})
        
    
class Login(BaseHandler):
    
    def get(self):

        user = users.get_current_user()
        if user:
            print("encontrado",users.GetCurrentUser())
            self.render_template('index.html', {})
        else:
            print("no encontrado",users.GetCurrentUser())
            self.redirect(users.create_login_url(self.request.uri))
            
        self.render_template('index.html', {})
        
class Logout(BaseHandler):
    
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect(users.create_logout_url(self.request.uri))
        self.render_template('index.html', {})
        
class Oauth2(BaseHandler):
    def post(self):
        # (Receive token by HTTPS POST)
        # ...

        try:
            id=self.request.get('id_token')
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(id, requests.Request(), CLIENT_ID)
    
            # Or, if multiple clients access the backend server:
            # idinfo = id_token.verify_oauth2_token(token, requests.Request())
            # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
            #     raise ValueError('Could not verify audience.')
        
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
    
            # If auth request is from a G Suite domain:
            # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
            #     raise ValueError('Wrong hosted domain.')
        
            # ID token is valid. Get the user's Google Account ID from the decoded token.
            userid = idinfo['sub']
        except ValueError:
        # Invalid token
            pass
    
#----------------------------------------
#------CRUD MODULO
#----------------------------------------
class BorrarModulo(BaseHandler):
    def get(self, modulo_id):
        iden = int(modulo_id)
        mod = db.get(db.Key.from_path('Modulo', iden))
        campanyas = mod.listaCampanyas #BORRADO CASCADA
        for c in campanyas:
            db.delete(c)
        db.delete(mod)
        #Recarga todo
        self.render_template('success.html', {})
        
class CrearModulo(BaseHandler):
        def post(self):
            nombre=self.request.get('nombreModulo')
            alpha=self.request.get('alpha')
            beta=self.request.get('beta')
            gamma=self.request.get('gamma')
            kappa=self.request.get('kappa')
            idealidad=self.request.get('idealidad')
            resistencia=self.request.get('resistencia')
            rendimiento=self.request.get('rendimiento')
            localizacion = db.GeoPt(float(self.request.get('latitud')), float(self.request.get('longitud')))
            
            Mod = Modulo(nombremodulo =nombre,
                         valoralpha = float(alpha),
                         valorbeta  = float(beta),
                         valorgamma = float(gamma),
                         valorkappa = float(kappa),
                         idealidad  = float(idealidad),
                         resistencia = float(resistencia),
                         rendimiento = float(rendimiento),
                         localizacion = localizacion)
            Mod.put()
            return webapp2.redirect('/')

        def get(self):
            self.render_template('crearModulo.html', {})

class EditarModulo(BaseHandler):

    def post(self, add_id):
        iden = int(add_id)
        Mod = db.get(db.Key.from_path('Modulo', iden))
        print("jaja si ", Mod.nombremodulo)
        Mod.nombremodulo=self.request.get('nombreModulo')
        print("jaja si ", Mod.nombremodulo)
        Mod.valoralpha=float(self.request.get('alpha'))
        Mod.valorbeta=float(self.request.get('beta'))
        Mod.valorgamma=float(self.request.get('gamma'))
        Mod.valorkappa=float(self.request.get('kappa'))
        Mod.idealidad=float(self.request.get('idealidad'))
        Mod.resistencia=float(self.request.get('resistencia'))
        Mod.rendimiento=float(self.request.get('rendimiento'))
        Mod.localizacion = db.GeoPt(float(self.request.get('latitud')), float(self.request.get('longitud')))
            
        Mod.put()
        print("jaja si ", iden)
        return webapp2.redirect('/')

    def get(self, add_id):
        iden = int(add_id)
        mod = db.get(db.Key.from_path('Modulo', iden))
        self.render_template('editarModulo.html', {'mod': mod})
        
                              
      
#----------------------------------------
#------CRUD CAMPANYA
#----------------------------------------
class ListaCampanyas(BaseHandler):
    def get(self):
        listaCampanyas = Campanya.all()
        self.render_template('listaCampanyas.html', {'listaCampanyas': listaCampanyas})
  
class CrearCampanya(BaseHandler):
    def post(self, mod_id):
        iden = int(mod_id)
        mod = db.get(db.Key.from_path('Modulo', iden))
        nombre=self.request.get('nombreCampanya')
        fechaCampanya =self.request.get('fechaCampanya')
        campanya = Campanya(modulo = mod,
                            fecha = datetime.strptime(fechaCampanya, '%Y-%m-%d'), 
                            nombrecampanya = nombre)
        campanya.put()
        return webapp2.redirect('/listaCampanyas')
    def get(self, mod_id):
        iden = int(mod_id)
        mod = db.get(db.Key.from_path('Modulo', iden))
        self.render_template('crearCampanya.html', {'mod': mod})
        
class EditarCampanya(BaseHandler):
    def post(self,cam_id):
        iden = int(cam_id)
        cam = db.get(db.Key.from_path('Campanya', iden))
        cam.fecha = datetime.strptime(self.request.get('fecha'), '%Y-%m-%d')
        cam.nombrecampanya = self.request.get('nombre')
        
        cam.put()
        listaCampanyas = Campanya.all()
        self.render_template('listaCampanyas.html', {'listaCampanyas': listaCampanyas})
     
    def get(self,cam_id):
        iden = int(cam_id)
        cam = db.get(db.Key.from_path('Campanya', iden))
        self.render_template('editarCampanya.html', {'cam': cam}) 

class BorrarCampanya(BaseHandler):
    def get(self,cam_id):
        iden = int(cam_id)
        cam = db.get(db.Key.from_path('Campanya', iden))
        db.delete(cam)
        
        webapp2.redirect('/listaCampanyas')
        return webapp2.redirect('/listaCampanyas')
#----------------------------------------
#------Mapa handler
#----------------------------------------
class MapHandler(BaseHandler):
    def get(self):
        data = '['
        listaModulos = Modulo.all()
        for x in listaModulos:
            data += "{lat: parseFloat("+str(x.localizacion.lat)+"), lng: parseFloat("+str(x.localizacion.lon)+")},"
        data+= ']'
        print("json: ",data)
        self.render_template('Map.html', {'data': data})
        
#----------------------------------------
#------Campanyas del modulo
#----------------------------------------
class CampanyasModulo (BaseHandler): 
    def get(self, mod_id):
        iden = int(mod_id)
        mod = db.get(db.Key.from_path('Modulo', iden))
        listaCampanyas = mod.listaCampanyas
        self.render_template('campanyasModulo.html', {'listaCampanyas': listaCampanyas})