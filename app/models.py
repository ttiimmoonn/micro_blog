from datetime import datetime
from app import db


'''
    Таблица пользователей определяет следующие поля:
        id - первичный ключ, тип Integer, параметр primary_key(значение генерируется БД)
        username - имя пользователя, типа String(64 длина), параметры index(индексируется) и unique(уникальное поле)
        relationship - Post(талица, которая представляет сторону "много"), author(добавляет метод для Post,
        чтобы вернуться к User)
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

# Метод вернет однозначное текстовое представление объекта класса User
    def __repr__(self):
        return '<User {}>'.format(self.username)


'''
    Таблица сообщений определяет следующие поля:
        id - первичный ключ, тип Integer, параметр primary_key(значение генерируется БД)
        user_id - id ющера который написал сообщение, ForeignKey(внешний ключ, который ведет к полю id
        таблици user
'''
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
