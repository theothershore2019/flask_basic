from flask import Flask
from flask import redirect
from flask import url_for
# import demo


# 创建flask的应用对象
# __name__表示当前的模块名字
# xxxx 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，tempaltes为模板目录
app = Flask(__name__)


@app.route("/")
def index():
    """定义的视图函数"""
    return "hello flask"


# 通过methods限定访问方式
@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"


# 同一路由装饰多个视图函数，在路径和请求方式一样的情况下，上面的会覆盖下面的。
@app.route("/hello", methods=["POST"])
def hello1():
    return "hello 1"


@app.route("/hello", methods=["GET"])
def hello2():
    return "hello 2"


# 同一视图由多个路由装饰，都可以访问。
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"


@app.route("/login")
def login():
    # url = "/"
    # 使用url_for的函数，通过视图函数的名字找到视图函数对应的url路径，也就是反向解析
    url = url_for("index")
    return redirect(url)


@app.route("/register")
def login():
    # url = "/"
    # 使用url_for的函数，最好传递所要跳转页面的视图函数的名称，而不是直接使用路径，
    # 如果跳转页面的路由修改了，我们依然可以跳转到指定页面，而不是牵一发而动全身，修改所有路由路径
    url = url_for("index")
    return redirect(url)


if __name__ == "__main__":
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    # 启动flusk程序
    app.run(host="0.0.0.0", port=5000, debug=True)


