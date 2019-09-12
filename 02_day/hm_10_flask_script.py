# 脚本扩展的使用
from flask import Flask

# 启动命令的管理类
from flask_script import Manager


app = Flask(__name__)


# 创建Manager管理类的对象
manager = Manager(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == "__main__":
    # app.run(debug=True)
    # 通过管理对象来启动flask
    manager.run()
