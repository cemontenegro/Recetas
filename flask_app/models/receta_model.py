from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app.models.usuario_model import Usuario
from datetime import date

class Receta:
	db='log_receta'
	def __init__(self, data):
		self.id = data['id']
		self.name = data['name']
		self.descripcion = data['descripcion']
		self.instruccion = data['instruccion']
		self.bajotreintamin = data['bajotreintamin']
		date_made=data['date_made']
		date_made=date_made.strftime('%Y-%m-%d')
		self.date_made = date_made
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']
		self.usuario_id = data["usuario_id"]
		self.usuario = data['usuario']

	@classmethod
	def crear_receta(cls, data):
		query = """ INSERT INTO recetas (name, descripcion, instruccion, bajotreintamin, date_made,created_at,updated_at, usuario_id) VALUES( %(name)s, %(descripcion)s, %(instruccion)s, %(bajotreintamin)s, %(date_made)s,NOW(),NOW(), %(usuario_id)s);"""
		return connectToMySQL('log_receta').query_db(query, data)


	@classmethod
	def todas_recetas(cls):
		query = "SELECT recetas.*,usuarios.nombre as usuario FROM recetas inner join usuarios on recetas.usuario_id=usuarios.id;"
		resultado = connectToMySQL(cls.db).query_db(query)
		todas_las_recetas = []
		for receta in resultado:
			todas_las_recetas.append(cls(receta))
		return todas_las_recetas


	@classmethod
	def recetas_con_usuarios(cls):
		consulta = "SELECT recetas.*,usuarios.nombre as usuario FROM recetas JOIN usuarios ON recetas.usuario_id = usuarios.id;"
		resultado = connectToMySQL(cls.db).query_db(consulta)
		todas_las_recetas_con_usuarios = []
		for receta in resultado:
			objeto_receta = cls(receta)
			objeto_receta.usuario.append(Usuario(receta))
		todas_las_recetas_con_usuarios.append(objeto_receta)
		return todas_las_recetas_con_usuarios 

	@classmethod 
	def receta_by_id(cls,data):
		consulta = "SELECT recetas.*,usuarios.nombre as usuario FROM recetas  JOIN usuarios ON recetas.usuario_id = usuarios.id WHERE recetas.id= %(id)s;"
		resultado = connectToMySQL(cls.db).query_db(consulta, data)
		return cls(resultado[0])

	@classmethod 
	def update_receta(cls,data): 
		consulta = "UPDATE recipes SET name=%(name)s, description= %(descripcion)s,  date_made=%(date_made)s, under= %(bajotreintamin)s,  instruccion=%(instruccion)s  WHERE id= %(receta_id)s;"
		resultado = connectToMySQL(cls.db).query_db(consulta, data)

	@classmethod
	def delete_receta(cls,data):
		consulta = "DELETE from recetas WHERE id= %(receta_id)s;"
		resultado = connectToMySQL(cls.db).query_db(consulta, data)