from google.appengine.ext import db


	
#Entidad modulo	
class Modulo(db.Model):
	nombremodulo = db.StringProperty()
	valoralpha = db.FloatProperty()
	valorbeta  = db.FloatProperty()
	valorgamma = db.FloatProperty()
	valorkappa = db.FloatProperty()
	idealidad  = db.FloatProperty()
	resistencia = db.FloatProperty()
	rendimiento = db.FloatProperty()
	localizacion = db.GeoPtProperty() #se compone de dos floats lat y lon se pueden contruir con moduloPrueba.localizacion(34.5, 12.3)

#Entidad campanya
class Campanya(db.Model):
	modulo = db.ReferenceProperty(Modulo, collection_name='listaCampanyas')
	fecha = db.DateTimeProperty()
	nombrecampanya = db.StringProperty()

class Usuario(db.Model):
	nombreusuario = db.StringProperty()
	email = db.EmailProperty()

class Comentario(db.Model):
	usuario = db.ReferenceProperty(Usuario, collection_name='listaComentarios')
	comentario = db.TextProperty()
	
#FUNCIONAMIENTO DE LA ESCRITURA
#Se rellena el atributo modulo como cualquier otro al hacer put

#Ejemplo:
#Creamos la entidad modulo
# 		Modulo(nombremodulo = 'MOD1', valoralpha = 12.2, valorbeta = 33.9, etc)
#		
#Creamos la campanya asociada a ese modulo
# 		Campanya(modulo = MOD1, fecha = 10/10/10, nombrecampanya = 'Dic10').put()


#FUNCIONAMIENTO DE LA LECTURA
#		print for c in  MOD1.listaCampanyas:
# 				print 'nombre: %s' % (c.nombre)
#				print 'fecha: %s' % (c.fecha)

#Info completa en https://cloud.google.com/appengine/articles/modeling
