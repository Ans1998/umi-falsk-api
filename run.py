#!flask/bin/python
# -*- coding: utf-8 -*-

# from blog2 import app # routes.index包引入了app

from routes.index import *

if __name__ == '__main__':
    app.run(debug=True)