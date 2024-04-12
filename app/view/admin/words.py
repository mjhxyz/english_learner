from flask import Blueprint, render_template, request, jsonify

from . import admin_required
from app.models.word import Word, db

admin_words_bp = Blueprint('/admin/words', __name__)


@admin_words_bp.route('/', methods=['GET'])
@admin_required
def index():
    return render_template('admin/words.j2')


@admin_words_bp.route('/add', methods=['GET'])
def add():
    return render_template('admin/form/words/add.j2')


@admin_words_bp.route('/do_add', methods=['POST'])
def do_add():
    data = request.json
    word = Word()
    word.word = data['word']
    word.cn = data['cn']
    db.session.add(word)
    db.session.commit()
    return jsonify({'ok': True})


@admin_words_bp.route('/delete', methods=['POST'])
def delete():
    data = request.json
    record_id = data['id']
    Word.query.filter(Word.id == record_id).delete()
    db.session.commit()
    return jsonify({'ok': True})
