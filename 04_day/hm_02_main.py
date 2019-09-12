from flask import Flask
from hm_03_users import register
from hm_04_goods import get_goods
from hm_05_orders import app_orders
from cart import app_cart
# 循环引用，解决方法，推迟一方的导入，让另外一方先执行


app = Flask(__name__)

# 装饰器解决循环引用死锁问题
app.route("/register")(register)
app.route("/get_goods")(get_goods)

# 注册蓝图
# app.register_blueprint(app_orders)
#注册蓝图，第一个参数app_orders是蓝图对象，url_prefix参数默认值是根路由，如果指定，会在蓝图注册的路由url中添加前缀。
app.register_blueprint(app_orders, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)

