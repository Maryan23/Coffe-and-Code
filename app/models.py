from sqlalchemy.orm import backref
from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(100),nullable = False,unique = True)
    username = db.Column(db.String(100))
    bio = db.Column(db.String(255))
    avatar = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.String)
    context = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    upvote = db.relationship('Upvote',backref='post',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='post',lazy='dynamic')
    comment = db.relationship('Comment',backref='post',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Blog{self.category}'

class Upvote(db.Model):
    _tablename_ = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls, id):
        upvote = Upvote.query.filter_by(blog_id=id).all()
        return upvote

    def _repr_(self):
        return f'{self.blog_id}'


class Downvote(db.Model):
    _tablename_ = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        downvote = Downvote.query.filter_by(blog_id=id).all()
        return downvote

    def _repr_(self):
        return f'{self.blog_id}'