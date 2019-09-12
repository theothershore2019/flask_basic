from flask import Flask
from flask import request
from flask import abort
from flask import Response
from flask import make_response

app = Flask(__name__)


@app.route("/index")
def index():
    # 1.使用元组，返回自定义的相应信息
    # 顺序不能错
    #      响应体       状态码                   响应头
    # return "index page", 400, [("Itcast", "python"), ("city", "shenzhen")]
    # return "index page", 400, {"Itcast": "python", "city": "shenzhen"}
    # return "index page", 666, {"Itcast": "python", "city": "shenzhen"}
    # return "index page", "666 itcast status", {"Itcast": "python", "city": "shenzhen"}
    # return "index page", "666 itcast status"

    # 2.使用make_response来构造相应信息
    resp = make_response("index page 2")
    
    # 设置状态码
    resp.status = "404 not found"

    # 设置响应头
    resp.headers["city"] = "chengdu"

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

