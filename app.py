from flask import Flask
from models import models
from common import config

from flask_wtf.csrf import CSRFProtect

def create_app():
    # 플라스크 인스턴스 생성
    app = Flask(__name__)

    # crsf
    # Enable CSRF protection globally for a Flask app.
    csrf = CSRFProtect()
    csrf.init_app(app)

    # 컨트롤러 임포트
    from controller import main
    from controller import usermanage

    # 블루프린트 등록
    app.register_blueprint(main.bp)
    app.register_blueprint(usermanage.bp)

    return app

# 데이터베이스 연동 및 테이블 생성
def set_database(app):
    app.config.from_object(config)

    # ORM(sqlalchemy) 객체가 담긴 변수(전역변수) 가져오기
    db = models.db       # models디렉토리의 model 파이썬 파일에서 db 변수 가져오기

    # DB 생성
    db.init_app(app)    # sqlalchemy를 app에 적용

    # DB 와 플라스크앱 연동
    db.app = app        # sqlalchemy의 엔진 연결 정보, 테이블 정보 불러옴

    # DB에 Model 기반으로 테이블 생성
    db.create_all()     # DB 없으면 새로 생성

    return app


if __name__ == '__main__':
    ### 플라스크앱(객체) 생성
    app = create_app()

    ### DB 세팅 된 플라스크앱(객체)
    app = set_database(app)

    ### 플라스크앱(객체) 실행
    app.run(host='0.0.0.0', port=8888, debug=True)  # debug=True : 소스코드를 변경 자동으로 감지 Flask서버 재시작