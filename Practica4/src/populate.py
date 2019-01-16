'''
Created on 15 ene. 2019

@author: Alberto
'''
from datetime import datetime
import os
import webapp2
import jinja2

from google.appengine.ext import db

from models import Modulo, Campanya, Usuario, Comentario 

class Populate():
    def addData(self):
        #ESTO ES PARA INICIALIZAR LA BASE DE DATOS
        q = db.GqlQuery("SELECT * FROM Modulo")
        resetearModulos= q.fetch(10)
        db.delete(resetearModulos)
        modulo1 = Modulo(nombremodulo ='Modulo1',
                         valoralpha = 1.2,
                         valorbeta  = 3.4,
                         valorgamma = 9.3,
                         valorkappa = 39.2,
                         idealidad  = 100.0,
                         resistencia = 39.4,
                         rendimiento = 20.0,
                         localizacion = db.GeoPt(52.37, 4.88)) #hay un rango de valores algo estrecho
        modulo2 = Modulo(nombremodulo ='Modulo2',
                         valoralpha = 1.4,
                         valorbeta  = 3.6,
                         valorgamma = 32.1,
                         valorkappa = 31.1,
                         idealidad  = 10.0,
                         resistencia = 30.4,
                         rendimiento = 65.0,
                         localizacion = db.GeoPt(12.37, 87.88))
        modulo1.put()
        modulo2.put()
        
        q1 = db.GqlQuery("SELECT * FROM Campanya")
        resetearCampanyas= q1.fetch(10)
        db.delete(resetearCampanyas)
        
        campanya1 = Campanya(modulo = modulo1, fecha = datetime(2018,12,30), nombrecampanya ='Dic18')
        campanya2 = Campanya(modulo = modulo1, fecha = datetime(2018,11,30), nombrecampanya ='Nov18')
        campanya3 = Campanya(modulo = modulo1, fecha = datetime(2018,11,30), nombrecampanya ='Nov18')
        campanya4 = Campanya(modulo = modulo1, fecha = datetime(2018,7,30), nombrecampanya ='Jul18')
        campanya5 = Campanya(modulo = modulo2, fecha = datetime(2018,9,30), nombrecampanya ='Sep18')
        campanya6 = Campanya(modulo = modulo2, fecha = datetime(2018,8,30), nombrecampanya ='Ago18')
        campanya7 = Campanya(modulo = modulo2, fecha = datetime(2018,1,30), nombrecampanya ='Ene18')
        campanya8 = Campanya(modulo = modulo2, fecha = datetime(2017,12,30), nombrecampanya ='Dic17')
        
        campanya1.put()
        campanya2.put()
        campanya3.put()
        campanya4.put()
        campanya5.put()
        campanya6.put()
        campanya7.put()
        campanya8.put()
        
        q1 = db.GqlQuery("SELECT * FROM Usuario")
        resetearUsuarios= q1.fetch(10)
        db.delete(resetearUsuarios)
        
        usuario1 = Usuario(nombreusuario = 'juanito1',
                         email  = 'remedans@gmail.com')
        usuario2 = Usuario(nombreusuario = 'juanito2',
                         email  = 'remedans1@gmail.com')
        usuario3 = Usuario(nombreusuario = 'pruebaparaingweb',
                         email  = 'pruebaparaingweb@gmail.com')
        
        usuario1.put()
        usuario2.put()
        usuario3.put()
        
        q2 = db.GqlQuery("SELECT * FROM Comentario")
        resetearComentarios= q2.fetch(10)
        db.delete(resetearComentarios)
        
        comentario1 = Comentario(usuario = usuario1, comentario = 'esto esta bien')
        comentario1.put()
        
        
        
        
        
        #FIN DE INICIALIZACION DE LA BASE DE DATOS