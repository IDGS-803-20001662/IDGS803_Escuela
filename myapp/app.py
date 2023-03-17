import flask
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from Alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import maestros
from models import db 

app = flask.Flask(__name__)
app.config.from_object(DevelopmentConfig) # generar configuracion de bd ( servidor, usuario, pass, puesto), cadena de conexion
csrf = CSRFProtect()
app.config['DEBUG'] = True

@app.route("/", methods = ['GET'])
def homes():
    return flask.jsonify({'Datos': 'Home'})

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(maestros)

if __name__ =='__main__':
    csrf.init_app(app)
    db.init_app(app) # inicia la conexion en base de datos
    with app.app_context():
        db.create_all() # analizar archivo config para corroborar que esten mapeado, sino, crea el mapeo
    app.run(port=3000)