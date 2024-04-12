from flask import Blueprint, render_template, request, jsonify

from . import admin_required
from app.models.book import Book, db
from app.models.book_word import BookWord

admin_books_bp = Blueprint('/admin/books', __name__)


@admin_books_bp.route('/', methods=['GET'])
@admin_required
def index():
    return render_template('admin/books.j2')


@admin_books_bp.route('/list', methods=['GET'])
@admin_required
def _list():
    args = request.args
    page = int(args['page'])
    limit = int(args['limit'])
    keyword = args.get('keyword')
    q = Book.query
    if keyword:
        q = q.filter(Book.name.like('%' + keyword + '%'))
    page_result = q.order_by(Book.hot.desc()).paginate(page=page, per_page=limit)
    items = list(map(lambda x: x.to_dict(), page_result.items))
    data = {
        "code": 0,
        "msg": "",
        "count": page_result.total,
        "data": items
    }
    return jsonify(data)


@admin_books_bp.route('/add', methods=['GET'])
@admin_required
def add():
    return render_template('admin/form/books/add.j2')


@admin_books_bp.route('/do_add', methods=['POST'])
def do_add():
    data = request.json
    book_word_list = []
    book = Book()
    book.name = data['name']
    db.session.add(book)
    db.session.flush()
    for word_id in data['word_ids']:
        book_word = BookWord()
        book_word.book_id = book.id
        book_word.word_id = word_id
        book_word_list.append(book_word)
    db.session.add_all(book_word_list)
    db.session.commit()
    return jsonify({'ok': True})


@admin_books_bp.route('/delete', methods=['POST'])
def delete():
    data = request.json
    record_id = data['id']
    Book.query.filter(Book.id == record_id).delete()
    BookWord.query.filter(BookWord.book_id == record_id).delete()
    db.session.commit()
    return jsonify({'ok': True})
