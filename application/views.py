"""Views of the web application."""

from flask import Flask, render_template, flash, redirect
from .forms import LoginForm

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index')
def index(user=None):
    """Render an index."""
    title = 'INDEX'
    user = 'euroclicheafficionado1'
    posts = [
        {
            'author': 'Miguel',
            'body': 'Este blog no es muy interesante, no?'
        },
        {
            'author': 'Francois',
            'body': 'Je suis un massive stereotype'
        }
    ]
    kwargs = dict(title=title, posts=posts, user=user)
    return render_template('index.html', **kwargs)


@app.route('/stocks/')
def loop():
    """Practice for loops in web page."""
    stocks = [
        {"symbol": "KO", "price": 43.2},
        {"symbol": "DIS", "price": 106.69},
        {"symbol": "BP", "price": 457.05}
    ]
    return render_template("stocks.html", data=stocks)


@app.route('/layout/<child_name>')
def child(child_name):
    """Practice template inheritance."""
    template_name = child_name + '.html'
    return render_template(template_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Render a simple login form."""
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId={}, remember_me={}'
              .format(form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
