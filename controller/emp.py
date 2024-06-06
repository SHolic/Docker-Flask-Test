from flask import Blueprint, render_template
import db.emp

emp = Blueprint("emp", __name__)

@emp.route("/emp/search-emp-list")
def search_emp_list():
    list = db.emp.search_emp_list()
    return render_template("emp.html", list=list)