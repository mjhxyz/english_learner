from flask import Blueprint, render_template, jsonify, request

from app.models.word import Word

words_api = Blueprint('words_api', __name__)


@words_api.route('/', methods=['GET'])
def index():
    args = request.args
    print(args['page'], args['limit'])
    page = int(args['page'])
    limit = int(args['limit'])
    keyword = args.get('keyword')
    # 分页查询 Word
    q = Word.query
    if keyword:
        q = q.filter(Word.word.like('%' + keyword + '%'))
    page_result = q.paginate(page=page, per_page=limit)
    print(page_result.__dict__)
    # items 转换为 dict
    items = list(map(lambda x: x.to_dict(), page_result.items))
    data = {
        "code": 0,
        "msg": "",
        "count": page_result.total,
        "data": items
    }
    return jsonify(data)
