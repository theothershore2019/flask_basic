from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/index")
def index():
    print("index 被执行")
    a = 1 / 0
    return "index page"


@app.route("/hello")
def hello():
    print("hello")
    return "hello page"


@app.before_first_request
def handle_before_first_request():
    """在第一次请求处理之前先被执行"""
    print("handle_before_first_request 被执行")


@app.before_request
def handle_before_request():
    """在每次请求之前都被执行"""
    print("handle_before_request 被执行")


# 后面两个钩子必须接受参数
# 是falsk将视图函数的返回值打包成一个响应对象，传递到钩子当中来
# 在这里对response进行什么操作都可以，操作之后要有返回值，并且返回给前端
@app.after_request
def handle_after_request(response):
    """在每次请求之后都被执行, 前提是视图函数没有出现异常"""
    print("handle_after_request 被执行")
    return response


@app.teardown_request
def handle_teardown_request(response):
    """在每次请求之后都被执行, 无论视图函数没有出现异常，工作在非调试模式时"""
    
    path = request.path
    if path == url_for("index"):
        print("在请求钩子中判断请求的视图逻辑: index")
    elif path == url_for("hello"):
        print("在请求钩子中判断请求的视图逻辑: hello")
    
    # print(request.path)
    print("handle_teardown_request 被执行")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

