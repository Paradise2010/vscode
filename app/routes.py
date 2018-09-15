from app import app
from flask import render_template, flash,redirect

from app.forms import LoginForm
@app.route("/")
@app.route("/index")
def index():
    user = {"username":"duke"}
    posts = [
        {
            'author':{'username':'liu'},
            'body':'this is templates example1'
        },
        {
            'author': {'username': 'zhongqiang'},
            'body': 'this is templates example2'
        }
    ]
    return render_template('index.html',title='my',user=user,posts=posts)
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("user login in as {}, do you need we to remember{}".format(form.username.data,form.remember_me.data))
        return redirect("/index")
    return render_template("login.html", title="login in", form=form)