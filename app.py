from flask import Flask, render_template

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template("index.html")

# صفحة تسجيل الدخول
@app.route('/login')
def login():
    return render_template("login.html")

# صفحة التسجيل
@app.route('/register')
def register():
    return render_template("register.html")


# مهم جداً
if __name__ == "__main__":
    app.run()