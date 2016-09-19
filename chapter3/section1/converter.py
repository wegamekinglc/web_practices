# -*- coding: utf-8 -*-
u"""
Created on 2016-9-19
@author: cheng.li
"""

import urllib
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConverter(BaseConverter):

    def __init__(self, url_map, separator='+'):
        super().__init__(url_map)
        self.separator = urllib.request.unquote(separator)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(
            BaseConverter.to_url(value) for value in values)


app.url_map.converters['list'] = ListConverter


@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return 'separator: {} {}'.format('+', page_names)


@app.route('/list2/<list(separator="|"):page_names>/')
def list2(page_names):
    return 'separator: {} {}'.format('|', page_names)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
