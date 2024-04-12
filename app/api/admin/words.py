from flask import Blueprint, jsonify, request

from app.models.word import Word

admin_words_api = Blueprint('admin_words_api', __name__)


@admin_words_api.route('/', methods=['GET'])
def index():
    args = request.args
    page = int(args['page'])
    limit = int(args['limit'])
    keyword = args.get('keyword')
    q = Word.query
    if keyword:
        q = q.filter(Word.word.like('%' + keyword + '%'))
    page_result = q.paginate(page=page, per_page=limit)
    items = list(map(lambda x: x.to_dict(), page_result.items))
    data = {
        "code": 0,
        "msg": "",
        "count": page_result.total,
        "data": items
    }
    return jsonify(data)
