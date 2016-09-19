# -*- coding: utf-8 -*-
u"""
Created on 2016-9-19
@author: cheng.li
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
