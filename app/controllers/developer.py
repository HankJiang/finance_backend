from flask import Blueprint

from app.common.api_tools import render_ok

bp = Blueprint('developer', __name__, url_prefix='/developer')


@bp.route('/load_stock', methods=['post'])
def load_stock():
    from app.tasks.stock_tasks import load_stock
    load_stock.apply_async()
    return render_ok()


@bp.route('/load_stock_history', methods=['post'])
def load_stock_history():
    from app.tasks.stock_tasks import load_stock_history
    load_stock_history.apply_async()
    return render_ok()

