from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.receta_model import Receta


@app.route('/crear_receta')
def formulario_receta():
	if 'usuario_id' not in session:
		return redirect('/')
	return render_template('crear_receta.html')

@app.route('/crear_receta', methods=['POST'])
def crear_receta():
	receta_id=Receta.crear_receta(request.form)
	return redirect("/dashboard")

@app.route('/editar/receta/<int:receta_id>')
def edit_receta(receta_id):
	data={
		"id":receta_id
	}
	receta=Receta.receta_by_id(data)
	return render_template('editar_receta.html',receta=receta)

@app.route('/editar/receta/<int:receta_id>',methods=['POST'])
def mod_receta(receta_id):
	data={
		"id":receta_id
	}
	Receta.update_receta(request.form)
	return redirect("/dashboard")

@app.route('/ver/receta/<int:receta_id>')
def ver_receta(receta_id):
	data={
		"id":receta_id
	}
	receta=Receta.receta_by_id(data)
	return render_template('vista_receta.html',receta=receta)


@app.route('/eliminar/receta/<int:receta_id>')
def del_receta(receta_id):
	data={
		"receta_id":receta_id
	}
	receta=Receta.delete_receta(data) 
	return redirect("/dashboard")