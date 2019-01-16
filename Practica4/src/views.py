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
    
    #----------------------------------------
    #------CRUD MODULO
    #----------------------------------------
class BorrarModulo(BaseHandler):
    def get(self, modulo_id):
        iden = int(modulo_id)
        mod = db.get(db.Key.from_path('Modulo', iden))
        #FALTARIA BORRADO CASCADA
        db.delete(mod)
        #Recarga todo
        listaModulos = Modulo.all()
        usuarios = Usuario.all()
        self.render_template('listaModulos.html', {'listaModulos': listaModulos, 'listaUsuarios':usuarios})
        
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
        
                              
class ListaCampanyas(BaseHandler):
    def get(self):
        listaCampanyas = Campanya.all()
        self.render_template('listaCampanyas.html', {'listaCampanyas': listaCampanyas})

    