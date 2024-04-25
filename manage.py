from datetime import timedelta
from flask import Flask

from configs.config import Config
from lib.util import register


def create_app(app_mode):
    app = Flask(__name__, static_url_path='')

    register(app, 'api.controllers.receive')
    register(app, 'app.view')
    register(app, 'app.controllers.main')
    register(app, 'app.controllers.cuisine')
    register(app, 'app.controllers.video')

    return app


if __name__ == '__main__':
    #import os

    #app_mode = os.getenv('ENV', 'development')
    app_mode = 'development'
    app = create_app(app_mode) 

    app.run(host="0,0,0,0", port=80, debug=True, use_reloader=True)
