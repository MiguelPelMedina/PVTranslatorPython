'''
Created on 15 ene. 2019

@author: Alberto
'''

from views import * 
import webapp2
from google.appengine.api import users

users.CreateLoginURL('/', _auth_domain=None, federated_identity=None)
users.CreateLogoutURL('/', _auth_domain=None)

app = webapp2.WSGIApplication([
        ('/', Inicio), 
        ('/listaModulos', ListaModulos), 
        ('/listaCampanyas', ListaCampanyas),
        ('/borrarModulo/([\d]+)', BorrarModulo),
        ('/editarModulo/([\d]+)', EditarModulo),
        ('/crearModulo', CrearModulo),
        ('/crearCampanya/([\d]+)', CrearCampanya),
        ('/editarCampanya/([\d]+)', EditarCampanya),
        ('/borrarCampanya/([\d]+)', BorrarCampanya),
        ('/map',MapHandler),
        ('/campanyasModulo/([\d]+)', CampanyasModulo),
        ('/login', Login),
        ('/logout', Logout)
        ],
        debug=True)

