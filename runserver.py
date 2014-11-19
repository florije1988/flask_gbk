# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Flask

app = Flask(__name__)

from app.app_main import app_main as app_main_blueprint
app.register_blueprint(app_main_blueprint, url_prefix='/main')

if __name__ == '__main__':
    app.run(host='0.0.0.0')