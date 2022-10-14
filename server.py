from flask_app.controllers import recetas_controller, usuarios_controller

from flask_app import app

if __name__=="__main__":
	app.run(debug=True)