from utils.AlchemyEncoder import AlchemyEncoder
# import json
# json.dumps 	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象
from multiprocessing import Process
import requests
import json
import datetime
import csv
import time
import os
from config import db
from apps.models.weiboCaptureRecord.index import WeiboCaptureRecord as CaptureRecord

class WeiboCaptureRecord(Process):
    def __init__(self, arr, Authorization):
        super().__init__()
        self.arr = json.loads(arr)
        self.Authorization = Authorization
        self.url = 'http://localhost:7001'
    def __repr__(self):
        pass
    def run(self):
        try:
            print('---子进程---', os.getppid(), os.getpid())
            arr = self.arr

            getUrl = arr['url']
            getUserIdPrefix = arr['userIdPrefix']
            scope = json.loads(arr['scope'])
            getUserStartId = scope['start']
            getUserEndId = scope['end']

            sum = int(getUserStartId)
            while sum < int(getUserEndId):
                sum = sum + 1
                userId = getUserIdPrefix + str(sum)
                self.weiBoFans(getUrl, userId)

            nowTime = datetime.datetime.now()
            updateTime = nowTime.strftime('%Y-%m-%d %H:%M:%S')

            # 修改
            obj = CaptureRecord.query.filter_by(userIdPrefix=getUserIdPrefix, scopeStart=getUserStartId, scopeEnd=getUserEndId).first()
            obj.update_time = updateTime  # 修改
            obj.status = 1  # 修改
            db.session.commit()  # 提交

            obj = json.dumps(obj, cls=AlchemyEncoder)
            data = {'code': '200', 'status': 'success', 'msg': '爬取成功', 'data': { 'content': obj }}
            print(data)

            headers = {
                'Authorization': self.Authorization
            }
            r = requests.post(self.url + '/api/notification/capture', headers=headers, data=data)
            print(r)
        except Exception as err:
            print(err)
            arr = self.arr
            getUserIdPrefix = arr['userIdPrefix']
            scope = json.loads(arr['scope'])
            getUserStartId = scope['start']
            getUserEndId = scope['end']
            # 修改
            nowTime = datetime.datetime.now()
            updateTime = nowTime.strftime('%Y-%m-%d %H:%M:%S')
            obj = CaptureRecord.query.filter_by(userIdPrefix=getUserIdPrefix, scopeStart=getUserStartId, scopeEnd=getUserEndId).first()
            obj.update_time = updateTime  # 修改
            obj.status = 2  # 修改
            db.session.commit()  # 提交

            obj = json.dumps(obj, cls=AlchemyEncoder)
            data = {'code': '405', 'status': 'fail', 'msg': '系统异常', 'data': { 'content':obj }}
            print(data)

            headers = {
                'Authorization': self.Authorization
            }
            r = requests.post(self.url + '/api/notification/capture', headers=headers, data=data)
            print(r)

    # 微博数据处理
    def weiBoFans(self, getUrl, getUserId):
        capture = True
        since_id = 1

        nowTime = datetime.datetime.now()
        filesName = datetime.datetime.now()

        while capture == True:
            since_id = since_id + 1
            time.sleep(3)
            # 第一步指定url
            url = getUrl + getUserId + '&since_id=' + str(since_id)
            # 第二步发送请求
            response = requests.get(url=url)
            # 第三步获取响应数据
            # pageData = json.loads(response.text)  # text返回的是字符串类型的数据(由响应体中的content-type,也可以是json)
            pageData = response.json()

            print('---userId---')
            print(getUserId)
            print(pageData)
            print('---since_id---')
            print(since_id)
            cardsLength = len(pageData['data']['cards'])
            print('---cardsLength---')
            print(cardsLength)

            if cardsLength > 0:
                res = pageData['data']['cards'][0]['card_group']
                # print('---res---')
                # print(res)
                for item in res:
                    # print('---item---')
                    # print(item)
                    item['create_time'] = nowTime.strftime('%Y-%m-%d %H:%M:%S')
                    self.createCsv(filesName, item)
            else:
                capture = False
    # 生成csv文件
    def createCsv(self, filesName, item):
        newFilesName = filesName.strftime('%Y%m%d%H%M%S') # 新的目录

        newFilesNamePath = './csv/' + str(newFilesName) # 新目录路径

        isNewFilesNameExists = os.path.exists(newFilesNamePath) # 判断新目录存在

        # 新目录不存在就新建
        if not isNewFilesNameExists:
            addFilesNamePath = newFilesNamePath
            os.mkdir(addFilesNamePath)

        nowTime = datetime.datetime.now()

        with open("./csv/" + newFilesName + "/"
                  + item['itemid'] + ".csv", 'w',
                  encoding="utf-8",
                  newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['data'])
            writer.writerow([json.dumps(item)])
            f.close()
