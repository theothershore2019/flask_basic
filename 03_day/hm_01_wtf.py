from flask import Flask, render_template, redirect, url_for, session
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import StringField, PasswordField, SubmitField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)

app.config["SECRET_KEY"] = "xhosd6f982yfhowefy29f"


class RegisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    #                       名字            验证器
    # DataRequired 保证数据必须填写，并且不能为空
    user_name = StringField(label="用户名", validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label="密码", validators=[DataRequired("密码不能为空")])
    password2 = PasswordField(label="确认密码", validators=[DataRequired("确认密码不能为空"),
                                                            EqualTo("password", "两次密码不一致")])
    submit = SubmitField(label="提交")


@app.route("/register", methods=["GET", "POST"])
def register():
    # 创建表单对象, 如果是post请求，前端发送了数据，flask会把数据在构造form对象的时候，存放到对象中
    form = RegisterForm()
    
    # 判断form中的数据是否合理
    # 如果form中的数据完全满足所有的验证器，则返回真，否则返回假
    if form.validate_on_submit():
        # 提取数据
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname, pwd, pwd2)
        session["user_name"] = uname
        
        return redirect(url_for("index"))
    
    return render_template("register.html", form=form)


@app.route("/")
def index():
    user_name = session.get("user_name", "")
    return "hello %s" % user_name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
