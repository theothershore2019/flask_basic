from flask import Flask, session


app = Flask(__name__)

# flask的session需要用到的秘钥字符串
app.config["SECRET_KEY"] = "dhsodfhisfhosdhf29fy989"


# flask默认把session保存到了cookie中
@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "python"
    session["mobile"] = "18611111111"
    return "login success"


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    mobile = session.get("mobile")
    return "hello %s, your phone is %s" % (name, mobile)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

