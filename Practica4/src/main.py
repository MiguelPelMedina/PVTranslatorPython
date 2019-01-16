'''
Created on 15 ene. 2019

@author: Alberto
'''
from views import Inicio, ListaModulos, ListaCampanyas, BorrarModulo, CrearModulo, EditarModulo #, Mapa, Comentarios, Imagenes
import webapp2

app = webapp2.WSGIApplication([
        ('/', Inicio), 
        ('/listaModulos', ListaModulos), 
        ('/listaCampanyas', ListaCampanyas),
        ('/borrarModulo/([\d]+)', BorrarModulo),
        ('/editarModulo/([\d]+)', EditarModulo),
        ('/crearModulo', CrearModulo)
        ],
        debug=True)