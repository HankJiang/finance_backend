from flask import Blueprint
import pandas_datareader as pdr

from app.common.api_tools import render_ok, params
from app.models import Stock


bp = Blueprint('stock', __name__, url_prefix='/stock')
@bp.route('/kline', methods=['get'])
def register():
    code, start, end = params('code', 'start', 'end')
    data = Stock.history(code, start, end)

    # if data:
    #     Stock.update_by_code(code, data)

    return render_ok(data)
