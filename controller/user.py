from flask import Blueprint, render_template

user = Blueprint('user', __name__)


@user.route('/user/login')
def login():
    return "登陆成功"


@user.route('/user/info')
def info():
    return render_template("user_info.html",
                           name="Scott",
                           sex="male",
                           age=26,
                           tel=["13312345678","15945872525"])
