from flask import Flask
from flask import jsonify
import json


app = Flask(__name__)


@app.route("/index")
def index():
    # json就是字符串
    data = {
        "name": "python",
        "age": 30
    }

    # json.dumps 将python中的字典转为json字符串
    # json.loads 将字符串转换为python中的字典
    # json_str = json.dumps(data)

    # return json_str, 200, {"Content-Type": "application/json"}
    
    # jsonify帮助转换json数据，并设置响应头Content-Type": "application/json"
    # return jsonify(data)
    return jsonify(city="cd", country="china")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

