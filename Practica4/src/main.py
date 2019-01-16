'''
Created on 15 ene. 2019

@author: Alberto
'''

from views import * 
import webapp2

app = webapp2.WSGIApplication([
        ('/', Inicio), 
        ('/listaModulos', ListaModulos), 
        ('/listaCampanyas', ListaCampanyas),
        ('/borrarModulo/([\d]+)', BorrarModulo),
        ('/editarModulo/([\d]+)', EditarModulo),
        ('/crearModulo', CrearModulo),
        #('/crearCampanya', CrearCampanya),
        ('/editarCampanya/([\d]+)', EditarCampanya),
        ('/borrarCampanya/([\d]+)', BorrarCampanya),
        ('/map',MapHandler)
        ],
        debug=True)

