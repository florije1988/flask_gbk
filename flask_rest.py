# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, Blueprint
from flask.ext import restful
import flask_restful

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}


demo_blueprint = Blueprint('demo_blueprint', __name__)

api = restful.Api(demo_blueprint, prefix="/blueprint")
api.add_resource(HelloWorld, "/helloworld")

app = Flask(__name__)
app.register_blueprint(demo_blueprint)

if __name__ == '__main__':
    app.run(debug=True)