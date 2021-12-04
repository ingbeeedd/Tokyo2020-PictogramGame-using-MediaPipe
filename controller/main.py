from flask import render_template, Blueprint
from flask import session 

bp = Blueprint('main',
               __name__,
               url_prefix='/')


# 요청 URL : http://127.0.0.1:8888/
@bp.route('/')
def main():
    print("메인 화면")
    userid = session.get('userid',None)
    return render_template('main.html', userid=userid)  # 이로써 뷰단(V)과 컨트롤러(C) 분리 -> MVC 패턴


