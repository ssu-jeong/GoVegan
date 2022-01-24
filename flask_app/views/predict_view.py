#### views.py
from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from flask_app.forms import ProductForm
from flask_app.models import Search,Product
from flask_app import db

bp = Blueprint("test", __name__, url_prefix="/pred")

@bp.route("/pred", methods=["GET", "POST"])
def Search_Product():
    form = ProductForm()
    if request.method == "POST" and form.validate_on_submit():
        # 클라이언트가 검색한 상품명
        search_product = form.product_name.data
        search = "%{}%".format(search_product)
        
        # 크롤링한 상품명 중, search가 포함된 모든 상품명을 리스트로 반환.
        products = Product.query.filter(Product.product_name.like(search)).all()
        print(products)
        # Search 테이블의 새로운 객체
        new_search = Search(search_name=search_product)
        db.session.add(new_search)
        db.session.commit()
        return render_template('products.html', form=form, products=products)
    else:
        form = ProductForm()

    return render_template('products.html', form=form, products=None)