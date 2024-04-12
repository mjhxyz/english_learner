from flask import Blueprint, render_template
from flask_login import login_required, current_user

from ..models.collection import Collection

collection_bp = Blueprint('collection_bp', __name__)


@collection_bp.route('/', methods=['GET'])
@login_required
def index():
    return render_template('collection.j2')
