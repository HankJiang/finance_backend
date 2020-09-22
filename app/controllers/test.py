from flask import Blueprint

from app.common.api_tools import render_ok

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/', methods=['get'])
def test():
    from app.tasks.stock_tasks import load_stock_history
    load_stock_history()
    return render_ok()

