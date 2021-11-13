from . import main
from flask import render_template,abort,redirect,url_for
from flask_login import login_required,current_user
from ..models import User
from .. import db
from .forms import UpdateProfile

#Views
@main.route('/')
def index():
    '''
    View root page function
    '''
    title = 'Coffee and Code'
    user = User.query.all()

    return render_template ('index.html',title=title,user=user)

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