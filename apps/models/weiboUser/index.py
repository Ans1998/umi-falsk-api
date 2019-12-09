from config import db

# User模型，它会跟相应的一个 react_user_info 表进行交互
class WeiboUser(db.Model):
    __tablename__  = 'weibo_user'
    id = db.Column(db.INTEGER, primary_key=True)
    weibo_id = db.Column(db.String(255))
    weibo_name = db.Column(db.String(255))
    weibo_profile =  db.Column(db.String(255))
    verified = db.Column(db.String(255))
    verified_type = db.Column(db.String(255))
    follow_count = db.Column(db.String(255))
    description = db.Column(db.String(255))
    close_blue_v = db.Column(db.String(255))
    create_time = db.Column(db.String(255))

    # def __init__(self, name, password, status):
    #     self.name = name
    #     self.password = password
    #     self.status = status