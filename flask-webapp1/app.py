from flask import Flask
from flask import render_template
from flask import url_for
from jalali.Jalalian import jdate




app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    date = jdate("r")
    return render_template('home.html' , date = date , page_title = "Home")



@app.route('/about_us')
def about_us():
    return render_template('about.html' , page_title = "About Us")



@app.route('/register')
def register():
    return render_template('register.html' , page_title = "Register")

if __name__ == '__main__':
    app.run(debug=True)

