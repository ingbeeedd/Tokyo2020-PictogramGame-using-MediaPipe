from flask import render_template, Blueprint
from flask import session
from sqlalchemy import func

from common.form import RegisterForm, LoginForm
from models.models import User
from models.models import db

import datetime

bp = Blueprint('usermanage',
               __name__,
               url_prefix='/user')

# 요청 URL : http://127.0.0.1:8888/user/register
@bp.route('/register', methods=['GET', 'POST']) #GET(정보보기), POST(정보수정) 메서드 허용
def register():
    form = RegisterForm()
    if form.validate_on_submit(): #유효성 검사. 내용 채우지 않은 항목이 있는지까지 체크
        
        now = datetime.datetime.now()

        usertable = User(
            userid = form.data.get('userid'),
            password = form.data.get('password'),
            create_date = now
        ) 

        db.session.add(usertable) #DB저장
        db.session.commit() #변동사항 반영
        
        return "<script type='text/javascript'> " \
               "alert('["+form.data.get('userid')+"] 회원이 로그인 됐습니다. 확인버튼 클릭하면 메인 페이지로 이동 합니다.'); " \
               "location.replace('/'); " \
               "</script>"
               
    return render_template('register.html', form=form) #form이 어떤 form인지 명시한다

# 요청 URL : http://127.0.0.1:8888/user/login
@bp.route('/login', methods=['GET','POST'])  
def login():
    form = LoginForm() #로그인폼
    if form.validate_on_submit(): #유효성 검사
        print('{}가 로그인 했습니다'.format(form.data.get('userid')))
        session['userid']=form.data.get('userid') #form에서 가져온 userid를 세션에 저장
        # return redirect('/') 

        #성공하면 main.html로
        return "<script type='text/javascript'> " \
               "alert('["+form.data.get('userid')+"] 회원이 로그인 됐습니다. 확인버튼 클릭하면 메인 페이지로 이동 합니다.'); " \
               "location.replace('/'); " \
               "</script>"

    return render_template('login.html', form=form)

# 요청 URL : http://127.0.0.1:8888/user/logout
@bp.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    # return redirect('/')
    return "<script type='text/javascript'> " \
            "alert('로그아웃이 완료됐습니다. 확인버튼 클릭하면 메인 페이지로 이동 합니다.'); " \
            "location.replace('/'); " \
            "</script>"


@bp.route('/rank')
def rankpage():
    userid = session.get('userid',None)
    # my_rank= "SELECT USERID,SCORE DENSE_RANK() OVER(ORDER BY SCORE DESC) AS RANK"    

    # https://stackoverflow.com/questions/40635099/convert-rank-and-partition-query-to-sqlalchemy

    subquery = db.session.query( User,func.rank().over(order_by=User.score.desc()).label('rnk')).subquery() 

    res = db.session.query(subquery).filter(
        subquery.c.userid==userid
    )
    
    print(res.first())
    my_rank = res.first()[4]
    # scores = [User.query.score]
    # df = pandas.DataFrame([scores], columns=['score'])
    # df#.rank(self, axis = 0, method = 'dense', numeric_only = None, na_option = 'keep', ascending = True, pct = False)
    return render_template('rank.html', 
                            # sql=sql,
                            userid=userid,
                            my_rank=my_rank)
