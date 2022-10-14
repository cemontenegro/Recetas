from flask_app import app
from flask_app.models.receta_model import Receta
from flask_bcrypt import Bcrypt
from flask import request,flash,render_template,redirect,session 
from flask_app.models.usuario_model import Usuario


bcrypt = Bcrypt(app)

@app.route('/')
def index():
	return render_template("login_register.html")

@app.route('/register/user', methods=['POST'])
def register():

	pw_hash = bcrypt.generate_password_hash(request.form['password'])
	print(pw_hash)
	data = {
		"nombre": request.form['nombre'],
		"apellido": request.form['apellido'],
		"email": request.form['email'],
		"password" : pw_hash
	}
	if not Usuario.is_valid(request.form):
		return redirect('/')
	usuario_id = Usuario.save(data)
	session['usuario_id'] = usuario_id
	return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
	data = { "email" : request.form["email"] }
	usuario_in_db = Usuario.get_by_email(data)
	if not usuario_in_db:
		flash("Invalid Email/Password")
		return redirect("/")
	if not bcrypt.check_password_hash(usuario_in_db.password, request.form['password']):
		flash("Invalid Email/Password")
		return redirect('/')
	session['usuario_id'] = usuario_in_db.id
	return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
	data={
		"owner_id":session['usuario_id']
	}
	return render_template("dashboard.html", usuario=Usuario.get_by_id(data), todas_recetas_usuarios=Receta.todas_recetas())


@app.route('/logout')
def logout():
	if 'usuario_id' in session:
		del session['usuario_id']
	return redirect("/")