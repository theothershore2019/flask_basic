from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    """登录"""

    # 接收参数
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    # a = 1 / 0

    # 校验参数
    # ""  0  [] () {} None 在逻辑判断时都是假
    if not all([user_name, password]):
        # 表示name或password中有一个为空或者都为空
        resp = {
            "code": 1,
            "message": "invalid params"
        }
        return jsonify(resp)

    if user_name == "admin" and password =="python":
        resp = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(resp)

    else:
        resp = {
            "code": 2,
            "message": "wrong user name or password"
        }
        return jsonify(resp)


if __name__ == "__main__":
    app.run()

