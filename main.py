from flask import Flask, render_template
from wtf_form import MyForm
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.secret_key = "myPassword"
bootstrap = Bootstrap5(app)




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def make_login():
    #if request.method == "GET":
    form_python = MyForm()#show form to fill

    #else request.method == "POST":
    if form_python.validate_on_submit() is True:
        if form_python.email.data == "admin@email.com" and form_python.password.data == "12345678":
            email = form_python.email.data
            password = form_python.password.data
            return render_template('success.html', html_email=email, html_password= password)#Good credentials
        else:
            return render_template('denied.html')#Bad credentials

    return render_template('login.html', html_form=form_python)#"GET"


if __name__ == '__main__':
    app.run(debug=True)