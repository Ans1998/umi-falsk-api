from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

#创建项目对象
app = Flask(__name__)

# 解决跨域
CORS(app)
