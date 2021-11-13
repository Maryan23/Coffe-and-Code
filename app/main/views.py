from . import main
from flask import render_template,abort,redirect,url_for
from flask_login import login_required,current_user
from ..models import User,Blog
from .. import db
from .forms import UpdateProfile, BlogForm
#Views
@main.route('/')
def index():
    '''
    View root page function
    '''
    title = 'Coffee and Code'

    return render_template ('index.html',title=title)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    
    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user)

@main.route('/user/<name>/update',methods = ['GET','POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',name = user.username))

    return render_template('profile/update.html',form =form)

@main.route('/create_new',methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():
        category = form.category.data
        context = form.context.data
        new_blog = Blog(category=category,context=context)
        #saving new blog
        new_blog.save_blog()
        return redirect(url_for('main.index'))
    else:
        all_blogs = Blog.query.order_by(Blog.posted).all

    return render_template('blog.html',blog_form = form,blogs=all_blogs)
