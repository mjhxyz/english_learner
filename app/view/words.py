from flask import Blueprint, render_template

words_bp = Blueprint('words', __name__)


@words_bp.route('/', methods=['GET'])
def index():
    return render_template('words.j2')
