from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('shiki', __name__)

@bp.route('/')
def index():
    db = get_db()
    shikis = db.execute(
        'SELECT p.id, name, gender, created, role_id'
        ' FROM shiki s JOIN user role ON s.role_id = r.id'
        ' ORDER BY name'
    ).fetchall()
    return render_template('shiki/index.html', shikis=shikis)
