from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from sqlalchemy import and_

from app.models.collection import Collection, db

collection_api = Blueprint('collection_api', __name__)


@collection_api.route('/', methods=['GET'])
@login_required
def index():
    args = request.args
    page = int(args['page'])
    limit = int(args['limit'])
    keyword = args.get('keyword')
    # 分页查询 Collection
    user_id = current_user.id
    q = Collection.query
    page_result = q.order_by(Collection.add_time.desc()).filter(and_(Collection.user_id == user_id)).paginate(page=page,
                                                                                                              per_page=limit)
    items = list(map(lambda x: x.to_dict(), page_result.items))
    # 将 items 按照 type==1 和 type==2 进行拆分
    data = {
        "code": 0,
        "msg": "",
        "count": page_result.total,
        "data": items
    }
    return jsonify(data)
