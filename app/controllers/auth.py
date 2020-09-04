from flask import Blueprint, request, session, g
from werkzeug.security import check_password_hash, generate_password_hash
import functools

from app.common.api_tools import render_ok, render_err
from app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif User.get_or_none(User.username == username) is not None:
        error = 'User {} is already registered.'.format(username)

    if error is None:
        User.create(username=username, password=generate_password_hash(password)).save()
        return render_ok()

    return render_err(error)


@bp.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    error = None
    user = User.get_or_none(User.username == username)

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user.password, password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user.id
        return render_ok()

    return render_err(error)


@bp.route('/logout')
def logout():
    session.clear()
    return render_ok()


@bp.before_app_request
def load_logged_in_user():
    print(request.json)
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.get(id == user_id)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return render_err("Please login")

        return view(**kwargs)

    return wrapped_view
