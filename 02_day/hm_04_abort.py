from flask import Flask
from flask import request
from flask import abort
from flask import Response


app = Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def login():
    # name = request.form.get()
    # pwd = reques.form.get()
    name = ""
    pwd = ""
    if name != "cyd" or pwd != "root":
        # 使用abort函数可以立即终止视图函数的执行，并返回给前端特定的信息
        # 1.传递状态码信息，必须是标准的http状态码
        abort(404)

        
        # 2.传递响应体信息，要封装成相应对象
        # resp = Response("login failed")
        # abort(resp)

    return "login success"


# 定义错误处理的方法
# 当flsak中出现返回的状态码是404信息的时候，自动调用下面的404函数
# 并将该函数的返回值作为页面的返回值信息
@app.errorhandler(404)
def handle_404_error(err):
    """自定义的处理错误方法"""
    # 这个函数的返回值会是前端用户看到的最终结果
    return "出现了404错误，错误信息：%s" % err


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

