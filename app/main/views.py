from . import main
from flask import render_template

#Views
@main.route('/')
def index():
    '''
    View root page function
    '''
    title = 'Coffee and Code'
    message = 'My coding journey with coffee'

    return render_template ('index.html',title=title,message=message)