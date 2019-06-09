from sanic import Sanic
from cca.routes import v1
from sanic_cors import CORS


def create_app():
    app = Sanic(__name__)
    app.blueprint(v1)
    cors = CORS(app, resources={f"/cca/*": {"origins": "*"}}, automatic_options=True)
    return app
