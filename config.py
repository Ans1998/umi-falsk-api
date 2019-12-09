from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'react_template'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)