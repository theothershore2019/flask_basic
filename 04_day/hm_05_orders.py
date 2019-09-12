from flask import Blueprint

# Blueprint必须指定两个参数，app_orders表示蓝图的名称，__name__表示蓝图所在模块
app_orders = Blueprint("app_orders", __name__)


@app_orders.route("/get_orders")
def get_orders():
    return "get orders page"


@app_orders.route("/post_orders")
def post_orders():
    return "post orders page"

