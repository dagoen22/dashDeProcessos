import flask
from blueprints.home_routes import home_routes

app = flask.Flask(__name__)

#Registro de rotas
app.register_blueprint(home_routes)

#rota default
@app.route('/')
def index():
    return flask.redirect('/home')

if __name__ == '__main__':
    app.run(debug='true',host='0.0.0.0')