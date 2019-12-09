#!flask/bin/python
# -*- coding: utf-8 -*-
from apps import app, jsonify, request, make_response
import json
# json.dumps 	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象
import os
from utils.AlchemyEncoder import AlchemyEncoder


from apps.services.test.index import Test
# from apps.services.test.index import reptileTest

from apps.services.WeiboCaptureRecord.index import WeiboCaptureRecord
from apps.services.testCourse.index import TestCourse
from apps.services.csv.index import Csv
from apps.services.csv.pushStorage import PushStorage

@app.route('/test', methods=['GET', 'POST'])
def testPage():
    result = Test.test()
    return result
    # return reptileTest()

@app.route('/test/aaa', methods=['GET', 'POST'])
def testCoursePage():
    p1 = TestCourse('alex')
    p2 = TestCourse('wupeiqi')
    p3 = TestCourse('yuanhao')

    p1.start()
    p2.start()
    p3.start()
    print('主进程', os.getpid(), os.getppid())
    return jsonify({'code': '405', 'status': 'fail', 'msg': 'xxxx', 'data': {}}), 200

@app.route('/weibo/capture', methods=['GET', 'POST'])
def weiboCapture():
    arr = json.loads(json.dumps(request.form, cls=AlchemyEncoder)) # 获取post过来的数据
    # print(arr)
    # print(request.headers)
    # if 'Authorization' in request.headers:
    #     return make_response(jsonify({'code': '405', 'status': 'fail', 'msg': 'token不正确', 'data': {}}), 200)
    if not arr or not 'url' in arr:
        return make_response(jsonify({'code': '405', 'status': 'fail', 'msg': '请求参数不正确', 'data': {} }), 200)
    try:
        Authorization = request.headers['Authorization']
        reptile = WeiboCaptureRecord(json.dumps(arr), Authorization)
        reptile.start()
        print('---主进程---', os.getpid(), os.getppid())
        return jsonify({'code': '200', 'status': 'success', 'msg': '爬虫请求执行中', 'data': {}}), 200
    except Exception as err:
        print(err)
        return jsonify({'code': '405', 'status': 'fail', 'msg': '系统异常', 'data': {}}), 200
#文件列表
@app.route('/weibo/file/list', methods=['GET', 'POST'])
def weiboFileList():
    try:
        csv = Csv()
        res = csv.getList()
        return jsonify({'code': '200', 'status': 'success', 'msg': '查询文件成功', 'data': res}), 200
    except Exception as err:
        print(err)
        return jsonify({'code': '405', 'status': 'fail', 'msg': '系统异常', 'data': {}}), 200
# 查看文件
@app.route('/weibo/look/file', methods=['GET', 'POST'])
def weiboLookFile():
    try:
        arr = json.loads(json.dumps(request.form, cls=AlchemyEncoder))  # 获取post过来的数据
        print(arr)
        csv = Csv()
        res = csv.getLookFiles(arr['cataloguePath'], arr['filePath'])
        # print(res)
        # print(type(res))
        return jsonify({'code': '200', 'status': 'success', 'msg': '查询成功', 'data': res}), 200
    except Exception as err:
        print(err)
        return jsonify({'code': '405', 'status': 'fail', 'msg': '系统异常', 'data': {}}), 200
# 删除文件
# [
#  {
#   'name': '20191128094533',
#   'file': [{'name': '20191128094541'}, { 'name': '20191128094538' }]
#  },
#  {
#   'name': '20191128094555',
#   'file': [{'name': '20191128094544'}]
#  }
#  ]
@app.route('/weibo/delete/file', methods=['GET', 'POST'])
def weiboDeleteFile():
    arr = json.loads(json.dumps(request.form, cls=AlchemyEncoder)) # 获取post过来的数据
    print(arr)

    if not arr or not 'form' in arr:
        return make_response(jsonify({'code': '405', 'status': 'fail', 'msg': '请求参数不正确', 'data': {}}), 200)
    try:
        csv = Csv()
        res = csv.getDeleteFiles(arr)
        return res
    except Exception as err:
        print(err)
        return jsonify({'code': '405', 'status': 'fail', 'msg': '系统异常', 'data': {}}), 200

# 文件进库
# [
#  {
#   'name': '20191128094533',
#   'file': [{'name': '20191128094541'}, { 'name': '20191128094538' }]
#  },
#  {
#   'name': '20191128094555',
#   'file': [{'name': '20191128094544'}]
#  }
#  ]
@app.route('/weibo/file/pushStorage', methods=['GET', 'POST'])
def weiboFilePushStorage():
    arr = json.loads(json.dumps(request.form, cls=AlchemyEncoder)) # 获取post过来的数据
    # print(arr)
    if not arr or not 'form' in arr:
        return make_response(jsonify({'code': '405', 'status': 'fail', 'msg': '请求参数不正确', 'data': {}}), 200)
    try:
        # form = eval(arr['form'])
        Authorization = request.headers['Authorization']
        pushStorage = PushStorage(arr, Authorization)
        pushStorage.start()
        print('---主进程---', os.getppid(), os.getpid())
        return jsonify({'code': '200', 'status': 'success', 'msg': '正在进库', 'data': {
            'content': json.dumps(arr)
        }}), 200
    except Exception as err:
        print(err)
        return jsonify({'code': '405', 'status': 'fail', 'msg': '系统异常', 'data': {}}), 200