from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    user = {'username': 'miguel'}
    return render_template('index.html', title='Home', user=user, posts=posts)


'''
    Функция описывает авторизацию в веб сервисе.
        "/login" - ссылка по которой происходит атворизция
        "methods" - методы разрешенные по этому адресу
        form - форма авторизации из файла forms.py
        form.validate_on_submit - проверка валидации данных отправленных форммой
            flash - методы выводящий предупреждения о результате валидации при верном заполнении
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('login'))
    return render_template('login.html', title='Sing In', form=form)

