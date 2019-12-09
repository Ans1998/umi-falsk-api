from config import db

# User模型，它会跟相应的一个 react_user_info 表进行交互
class WeiboCaptureRecord(db.Model):
    __tablename__  = 'weibo_capture_record'
    id = db.Column(db.INTEGER, primary_key=True)
    url = db.Column(db.String(255))
    status = db.Column(db.String(255))
    userIdPrefix =  db.Column(db.String(255))
    scopeStart = db.Column(db.String(255))
    scopeEnd = db.Column(db.String(255))
    create_time = db.Column(db.String(255))
    update_time = db.Column(db.String(255))

    # def __init__(self, name, password, status):
    #     self.name = name
    #     self.password = password
    #     self.status = status