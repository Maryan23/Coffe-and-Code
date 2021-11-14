from . import main
from flask import render_template,abort,redirect,url_for
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .. import db
from .forms import UpdateProfile, BlogForm,CommentForm
from flask_mail import Message 
#Views
@main.route('/')
def index():
    '''
    View root page function
    '''
    title = 'Coffee and Code'
    blogs = Blog.query.all()

    return render_template ('index.html',title=title,blogs=blogs)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    
    if user is None:
        abort(404)
    else:
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
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        all_blogs = Blog.query.order_by(Blog.posted).all

    return render_template('blog.html',blog_form = form,blogs=all_blogs)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html',comment_form =form, blog = blog,all_comments=all_comments)

