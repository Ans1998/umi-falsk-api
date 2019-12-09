from apps.models.test.index import User
from utils.AlchemyEncoder import AlchemyEncoder
import json
# json.dumps 	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象
class Test():
    def __init__(self):
        print('server __init__')
    def __repr__(self):
        print('server __repr__')
    def test():
        users = User.query.all()
        arr = json.loads(json.dumps(users, cls=AlchemyEncoder))
        data = {
            'code': '200',
            'msg': '爬取成功',
            'data': arr
        }
        return data

# #创建数据库与表
# db.create_all()
#
# #创建User对象并插入数据库
# admin = User('admin', 'admin@example.com')
# guest = User('guest', 'guest@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()
#
# #查询
# users = User.query.all()
# admin = User.query.filter_by(username='admin').first()
# all_results = User.query.filter_by(classID=key_classID, name=key_name).all()
# all_results = User.query.filter(
#      Students.st_id.like("%" + key_st_id + "%") if key_st_id is not None else "",
#      Students.name.like("%" + key_name + "%") if key_name is not None else "",
#      Students.remark.like("%" + key_remark + "%") if key_remark is not None else "",
#      Students.classID.like("%" + key_classID + "%") if key_classID is not None else ""
#  ).all()
#   all_results = Students.query.filter(
#             Students.remark.like("%" + key_remark + "%") if key_remark is not None else ""
#         ).all()

# py = Category('python')
# p = Post('Hello python!', 'pytho is pretty cool', py)
# db.session.add(py)
# db.session.add(p)
# db.session.commit()