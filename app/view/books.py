import json

from flask import Blueprint, render_template, request
from flask_login import login_required
from sqlalchemy import text

from ..models.book import Book, db
from ..models.word import Word

books_bp = Blueprint('books', __name__)


@books_bp.route('/', methods=['GET'])
@login_required
def index():
    return render_template('books.j2')


@books_bp.route('/read', methods=['GET'])
@login_required
def read():
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)
    result = db.session.execute(
        text('SELECT w.* FROM word w JOIN book_word bw ON w.id=bw.word_id AND bw.book_id=:book_id'),
        {'book_id': book_id}).fetchall(),
    words = []
    for res_list in result:
        if not res_list:
            continue
        for res in res_list:
            print('========>>>>>>', res)
            w = Word()  # 通过传递字典形式的结果值创建模型实例
            w.id = res[0]
            w.word = res[1]
            w.cn = res[2]
            w.add_time = res[3]
            w.update_time = res[4]
            words.append(w.to_dict())
    return render_template('read.j2', book=book, words=json.dumps(words, default=str))
