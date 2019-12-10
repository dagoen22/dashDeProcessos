import flask
import psutil

home_routes = flask.Blueprint('home',__name__,url_prefix='/home')

@home_routes.route('/')
def index():
    usuario = [x for x in psutil.users()]
    parametros_rota = {
        'usuario' : usuario[0].name,
        'memoria_total' : round(psutil.virtual_memory().total / (10 ** 9), 2),
        'memoria_usada' : round(psutil.virtual_memory().used / (10 ** 9), 2),
        'qtd_cpus' :psutil.cpu_count(),
        'montagem': psutil.disk_partitions()[0].mountpoint,
        'espaco_disco_livre': round(psutil.disk_usage('/').free  / (10 ** 9), 2),
        'espaco_disco_usado': round(psutil.disk_usage('/').used  / (10 ** 9), 2),
        'espaco_disco_total': round(psutil.disk_usage('/').total  / (10 ** 9), 2),
    }
    return flask.render_template('home.html', home = parametros_rota)