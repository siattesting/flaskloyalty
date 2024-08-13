from flask import Flask

from board.home import home
from board.partners import partners

def create_app():
    app = Flask(__name__)

    from . import db
    db.init_app(app)

    app.register_blueprint(home.bp)
    app.register_blueprint(partners.bp)

    return app

