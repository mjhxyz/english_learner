from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from sqlalchemy import and_

from app.models.book import Book, db
from app.models.collection import Collection

books_api = Blueprint('books_api', __name__)


@books_api.route('/collect', methods=['POST'])
@login_required
def collect():
    # 获取 json 数据
    data = request.get_json()
    book_id = data['book_id']
    user_id = current_user.id
    book = Book.query.filter_by(id=book_id).first()
    if not book:
        return jsonify({'error': 'Book not found'})
    # 检查是否已经收藏了
    coll = Collection.query.filter(
        and_(Collection.obj_id == book_id, Collection.user_id == user_id, Collection.type == 1)).first()
    if coll is None:
        # 添加收藏
        coll = Collection()
        coll.user_id = current_user.id
        coll.obj_id = book_id
        coll.type = 1
        coll.name = book.name
        db.session.add(coll)
        db.session.commit()
    return jsonify(data)


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
    # 获取 ids
    ids = map(lambda x: x['id'], items)
    # 查询已经收藏的 book
    collection_list = Collection.query.filter(
        and_(Collection.obj_id.in_(ids), Collection.type == 1, Collection.user_id == current_user.id)).all()
    # 获取已经收藏的 book 的 id set
    id_set = set(map(lambda x: x.obj_id, collection_list))
    # 如果 items 的 id 在 id_set 中，那么标记
    for book in items:
        book['collection'] = book['id'] in id_set

    data = {
        "code": 0,
        "msg": "",
        "count": page_result.total,
        "data": items
    }
    return jsonify(data)
