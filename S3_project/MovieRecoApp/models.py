### README
### models.py : DB 처리하는 파일

from flask_migrate import Migrate           # Migrate : git 처럼 업그레이드같은걸 할 수 있다
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


db = SQLAlchemy()
migrate = Migrate()

class Movies(db.Model):     # movies 테이블 생성

    __tablename__ = 'movies'    # tableName 지정

    id = db.Column(db.Integer(), nullable=False, primary_key=True)      # Id(Primary Key)
    title = db.Column(db.String(), nullable=False)                      # 영화제목
    pubDate = db.Column(db.Integer(), nullable=False)                   # 제작년도
    genre = db.Column(db.String(), nullable=False)                      # 장르
    director = db.Column(db.String(), nullable=True)                    # 감독
    publisher = db.Column(db.String(), nullable=True)                   # 제작사    
    rating = db.Column(db.Integer(), nullable=True)                     # 평점    
    poster = db.Column(db.String(), nullable=True)                      # 포스터

    mov = relationship('Actors', backref=db.backref('act'))

    def __repr__(self):
        return f"Movie id : {self.id}, title : {self.title}"
                                         
    
class Actors(db.Model):     # actors 테이블 생성

    __tablename__ = 'actors'    # tableName 지정
    
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    movie_title = db.Column(db.String(), db.ForeignKey('movies.title'), nullable=False)
    lead_actor1 = db.Column(db.String(), nullable=True)
    lead_actor2 = db.Column(db.String(), nullable=True)
    sub_actor1 = db.Column(db.String(), nullable=True)
    sub_actor2 = db.Column(db.String(), nullable=True)


    def __repr__(self):
        return f"Actor id : {self.id}"