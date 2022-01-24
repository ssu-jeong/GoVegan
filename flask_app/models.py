from flask_app import db

#크롤링한 csv import하는 빈 테이블 생성
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text, nullable=True)
    page_url = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.Text, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    clean_name = db.Column(db.Text, nullable=True)

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_name = db.Column(db.String(200), nullable=True)
    created_time = db.Column(db.DateTime, server_default=db.func.now())