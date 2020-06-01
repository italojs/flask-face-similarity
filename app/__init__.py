import appfly
from .config import config
from appfly.app import factory

def fn(_):
    # Routes files
    from app.presentation.http.routes import face

    # Routes rules
    appfly.add_url('/face', face.route, 'POST')

factory(fn, __name__, config["cors"])