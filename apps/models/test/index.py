from config import db

# User模型，它会跟相应的一个 react_user_info 表进行交互
class User(db.Model):
    __tablename__  = 'react_user_info'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    status = db.Column(db.String(255))
    creact_time = db.Column(db.String(255))

    # def __init__(self, name, password, status):
    #     self.name = name
    #     self.password = password
    #     self.status = status

    #定义__repr__方法：将对象的属性方法打印成一个可读字符串
    # def __repr__(self):
    #     return "{'id':'%s','name':'%s','password':'%s','status':%s,'creact_time':'%s'}" % (self.id, self.name, self.password, self.status, self.creact_time)