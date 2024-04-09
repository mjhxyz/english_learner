from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required

from app.models.book import Book
from app.models.collection import Collection

books_api = Blueprint('books_api', __name__)


@books_api.route('/', methods=['GET'])
@login_required
def index():
    args = request.args
    page = int(args['page'])
    limit = int(args['limit'])
    keyword = args.get('keyword')
    # 分页查询 Book
    q = Book.query
    if keyword:
        q = q.filter(Book.name.like('%' + keyword + '%'))
    page_result = q.order_by(Book.hot.desc()).paginate(page=page, per_page=limit)
    # items 转换为 dict
    items = list(map(lambda x: x.to_dict(), page_result.items))
    data = {
        "code": 0,
        "msg": "",
        "count": page_result.total,
        "data": items
    }
    return jsonify(data)
