import os
# import pymysql
from cv2 import minMaxLoc #디렉토리 절대 경로
from flask import Flask
from flask import render_template #template폴더 안에 파일을 쓰겠다
from flask import request #회원정보를 제출할 때 쓰는 request, post요청 처리
from flask import redirect
from sqlalchemy.sql.selectable import Select #리다이렉트
#from flask_sqlalchemy import SQLAlchemy
from models import db
from models import User
from flask import session #세션
from flask_wtf.csrf import CSRFProtect #csrf
from form import RegisterForm, LoginForm
from sqlalchemy import func
# import pandas
# import sqlite3
app = Flask(__name__)


@app.route('/')
def mainpage():
    userid = session.get('userid',None)
    return render_template('main.html', userid=userid)

# @app.route('/game') #game시 점수 업데이트하기
# def gamepage():
#     usertable.score = form.data.get('score')

# def get_ranking():

@app.route('/rank')
def rankpage():
    userid = session.get('userid',None)
    sql = len(User.query.all())
    my_rank= "SELECT USERID,SCORE DENSE_RANK() OVER(ORDER BY SCORE DESC) AS RANK"    

    # https://stackoverflow.com/questions/40635099/convert-rank-and-partition-query-to-sqlalchemy

    subquery = db.session.query( User,func.rank().over(order_by=User.score.desc()).label('rnk')).subquery() 

    res = db.session.query(subquery).filter(
        subquery.c.userid==userid
    )
    
    print(res.first())
    # my_rank = res.first()[4]
    # scores = [User.query.score]
    # df = pandas.DataFrame([scores], columns=['score'])
    # df#.rank(self, axis = 0, method = 'dense', numeric_only = None, na_option = 'keep', ascending = True, pct = False)
    return render_template('rank.html', sql=sql, userid=userid, my_rank=my_rank)
    

@app.route('/pose')
def create_app():
    app = Flask(__name__)
    from controller import main_controller
    app.register_blueprint(main_controller.bp)
    return render_template('pose.html')


@app.route('/register', methods=['GET', 'POST']) #GET(정보보기), POST(정보수정) 메서드 허용
def register():
    form = RegisterForm()
    if form.validate_on_submit(): #유효성 검사. 내용 채우지 않은 항목이 있는지까지 체크
        usertable = User() 
        usertable.userid = form.data.get('userid')
        usertable.password = form.data.get('password')
        db.session.add(usertable) #DB저장
        db.session.commit() #변동사항 반영
        
        return "회원가입 성공" 
    return render_template('register.html', form=form) #form이 어떤 form인지 명시한다

@app.route('/login', methods=['GET','POST'])  
def login():
    form = LoginForm() #로그인폼
    if form.validate_on_submit(): #유효성 검사
        print('{}가 로그인 했습니다'.format(form.data.get('userid')))
        session['userid']=form.data.get('userid') #form에서 가져온 userid를 세션에 저장
        return redirect('/') #성공하면 main.html로
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

if __name__ == "__main__":
    #데이터베이스---------
    basedir = os.path.abspath(os.path.dirname(__file__)) #현재 파일이 있는 디렉토리 절대 경로
    dbfile = os.path.join(basedir, 'db.sqlite') #데이터베이스 파일을 만든다

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #사용자에게 정보 전달완료하면 teadown. 그 때마다 커밋=DB반영
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추가 메모리를 사용하므로 꺼둔다
    app.config['SECRET_KEY']='asdfasdfasdfqwerty' #해시값은 임의로 적음

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app) #app설정값 초기화
    db.app = app #Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
    db.create_all() #DB생성

    app.run(host="127.0.0.1", port=5000, debug=True)