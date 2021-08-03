### config.py : 웹 개발을 할 때 필요한 환경설정들을 담은 파일입니다.

import os


BASE_DIR = os.path.dirname(__file__)    ## MovieRecoApp.db라는 DB파일을 프로젝트의 루트 디렉터리에 저장하는 옵션

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'MovieRecoApp.db'))  # DB 접속주소
SQLALCHEMY_TRACK_MODIFICATIONS = False                                                      # SQLAlchemy 이벤트 처리하는 옵션(변경사항을 추적해주는 것)

