from flask import Blueprint, render_template, jsonify, request

from app.view import words

words_api = Blueprint('words_api', __name__)


@words_api.route('/', methods=['GET'])
def index():
    args = request.args
    print(args['page'], args['limit'])
    page = int(args['page'])
    limit = int(args['limit'])
    keyword = args.get('keyword')
    # TODO DELETE
    # 随机数据
    res = []
    for i in range(limit):
        res.append({
            'id': f'W${str((page - 1) * limit + i + 1)}',
            'word': 'helloworld',
            'cn': '你好的' + str(keyword)
        })

    data = {
        "code": 0,
        "msg": "",
        "count": 1000,
        "data": res
    }
    return jsonify(data)
