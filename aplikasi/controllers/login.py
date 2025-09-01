from aplikasi import app, bcrypt
from flask import render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
# from aplikasi import db_connect
from aplikasi.dao.users.userdao import get_user_data 
from aplikasi.forms.formLogin import loginForm
from aplikasi.models.loginModels import Users
from aplikasi import toastr

@app.route('/login/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = loginForm()
    # validate_on_submit mengecek apabila request.method itu POST, PUT, DELETE. kalau get return false
    if form.validate_on_submit():
        get_user = get_user_data(form.email.data)   

        if get_user['result']:
            user_mod = Users()
            user_mod.email = get_user['result'][0][0]
            user_mod.name = get_user['result'][0][2]   
            user_mod.id = get_user['result'][0][3]   

            if bcrypt.check_password_hash(pw_hash=get_user['result'][0][1], password=form.password.data):
                if login_user(user_mod, remember=form.remember.data, force=True):
                    return redirect(url_for('home'))
            else:    
                flash('Password yang anda masukan salah', 'warning')

        else:
            flash('[Login] User tidak ditemukan', 'danger')    
    
    return render_template('login.html', form=form)


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))