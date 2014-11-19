# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import app_main
from flask import request


@app_main.route('/', methods=['POST'])
def do_main():
    raw_data = request.data or request.json
    if raw_data:
        print raw_data
        return raw_data