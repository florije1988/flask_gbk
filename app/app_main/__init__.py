# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Blueprint

app_main = Blueprint('app_main', __name__)

from . import views