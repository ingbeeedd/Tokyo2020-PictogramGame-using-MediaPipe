from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy() #SQLAlchemy를 사용해 데이터베이스 저장

class User(db.Model): #데이터 모델을 나타내는 객체 선언
    #테이블 이름
    __tablename__ = 'user_table' 
    
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    userid      = db.Column(db.String(32), unique=True, nullable=False)
    password    = db.Column(db.String(32), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    score       = db.Column(db.Integer)
    # 바로 query filter로 계산 가능
    # rank = db.Column(db.Integer)
    
    def __init__(self, userid=None, password=None, create_date=None):
        self.userid = userid
        self.password = password
        self.create_date = create_date

    def set_password(self, password):
        self.password = generate_password_hash(password)
 
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "password": self.password,
            "create_date": self.create_date,
            "score": self.score
        }