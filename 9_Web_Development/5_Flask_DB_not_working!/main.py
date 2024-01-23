# from attr import has
from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123@localhost:5432/testDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class loginPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String (50), nullable=False) 
    password = db.Column(db.String (50), nullable=False)
    date = db.Column(db.DateTime(),default=datetime.datetime.utcnow())

    def __init__(self,username,password):
        self.username = username
        self.password = password

# db.create_all()

@app.route('/regist')
def regist():
    # hash = generate_password_hash(request.form.get('password'))
    try:
        l = loginPage(username = request.form.get('username'),password =request.form.get('password'))
        db.session.add(l)
        db.session.commit()
    except :
        db.session.rollback()
    return render_template('regis.html')


if __name__ == ('__main__'):
    app.run(debug=True)