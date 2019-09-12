from flask import Flask
from flask import request


app = Flask(__name__)


# 接口api：所定义的特定路径以及包含了视图函数的一段后台的业务逻辑
# 47.103.135.225:5000/index?city=shenzhen&country=china 查询字符串 QueryString
@app.route("/index", methods=["GET", "POST"])
def index():
    # request中包含了前端发送过来的所有请求数据
    # form和data是用来提取请求体数据
    # 通过request.form可以直接提取请求体中的表单格式的数据，是一个类字典的对象
    # 通过get方法只能拿到多个同名参数中的第一个
    name = request.form.get("name")
    age = request.form.get("age")
    print("request.data: %s" % request.data)

    name_li = request.form.getlist("name")

    # args是用来提取url中的参数（查询字符串）
    city = request.args.get("city")
    return "hello name=%s age=%s city=%s name_li=%s" % (name, age, city, name_li)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

