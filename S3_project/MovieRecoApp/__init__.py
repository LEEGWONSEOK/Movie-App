### README
### __init__.py : 내가 작성한 pybo.py 과 같은 역할

from flask import Flask, render_template
from MovieRecoApp.models import db, migrate
import config

def create_app():                   # Application Factory 형태로 변경하기
    app = Flask(__name__)           # Flask Application 생성 코드   |   '__name__' : 모듈명
    app.config.from_object(config)  # app.config 환경변수 불러오기
    
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite+pysqlite:///MovieApp.db'
    
    ## ORM
    db.init_app(app)                        # flask_app 연결
    migrate.init_app(app, db)               # 
    
    ## Blueprint
    from MovieRecoApp.routes import main_route, list_route, search_route    # 순환되는 것을 방지하기 위해서 여기에 작성!
    
    app.register_blueprint(main_route.bp)
    #app.register_blueprint(list_route.bp)
    #app.register_blueprint(search_route.bp)
    
    from MovieRecoApp import models         # 
    
    return app                              # create_app 함수가 app 객체를 생성해 반환하도록 변경

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)                     # 디버그 설정해서 자동으로 재시작(정식서비스에서는 해제)