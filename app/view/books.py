from flask import Blueprint, render_template
from flask_login import login_required


books_bp = Blueprint('books', __name__)


@books_bp.route('/', methods=['GET'])
@login_required
def index():
    return render_template('books.j2')
