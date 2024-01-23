import psycopg2
from flask import Flask, request, render_template, flash, make_response
import key
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = key.KEY


@app.route('/cookie/')
def cookie():
    if not request.cookies.get('test'):
        res = make_response('Setting a cookie')
        res.set_cookie('test', '123', 60*60*24*365*2)
    else:
        req = request.cookies.get('test')
        res = make_response('Value of cookie test is {req}')
    return res


@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response(f'Cookie deleted')
    res.set_cookie('test', '123', max_age=0)
    return res


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if len(request.form['username']) == 0:
            flash('Please enter a username', category='error')
        elif len(request.form['username']) <= 2:
            flash('Username is too short. Try again', category='error')
        
        if valid_login(request.form['username'], request.form['password']):
            flash('Correct username and password',category='success')
            time.sleep(1)
            return recept()
        else:
            flash('Invalid username or password', category='error')
    return render_template('login.html')


def valid_login(name, password):
    if name == 'root' and password == 'pass':
        flash(f'Correct username and password', category='success')
        return True
    else:
        flash(f'Invalid username or password', category='error')
        return False


@app.route('/recept/')
def recept():
    return render_template('recept.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)