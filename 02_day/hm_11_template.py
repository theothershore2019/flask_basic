from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "python",
        "age": 18,
        "my_dict": {"city": "sz"},
        "my_list": [1, 2, 3, 4, 5],
        "my_int": 0
    }

    return render_template("index.html", **data)    
    # return render_template("index.html", name="xtu", age=60)


# 普通自定义过滤器
# li为过滤器中传递的参数，也就是模板中要过滤的变量
def list_step_2(li):
    """自定义的过滤器"""
    return li[::2]


# 注册过滤器
# li2是模板中所显示的过滤器名字，可以任意指定
app.add_template_filter(list_step_2, "li2")


# 装饰器自定义过滤器
@app.template_filter("li3")
def list_step_3(li):
    """自定义的过滤器"""
    return li[::3]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

