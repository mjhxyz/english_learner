from flask import Blueprint, render_template
from flask_login import login_required

words_bp = Blueprint('words', __name__)


@words_bp.route('/', methods=['GET'])
@login_required
def index():
    return render_template('words.j2')
