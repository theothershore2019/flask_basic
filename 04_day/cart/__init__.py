from flask import Blueprint

# Blueprint必须指定两个参数，app_cart表示蓝图的名称，__name__表示蓝图所在模块
# 第三个参数指定模板路径
app_cart = Blueprint("app_cart", __name__, template_folder="templates")

# 在__init__.py文件被执行的时候，把试图加载进来，让蓝图与应用程序知道有视图的存在
from .views import get_cart

