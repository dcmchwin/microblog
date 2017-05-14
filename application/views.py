from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def index(user=None):
    title = 'INDEX'
    if user is None:
        kwargs = dict(title=title)
    else:
        kwargs = dict(title=title, user=user)
    return render_template('index.html', **kwargs)


@app.route('/stocks/')
def loop():
    stocks = [
        {"symbol": "KO", "price": 43.2},
        {"symbol": "DIS", "price": 106.69},
        {"symbol": "BP", "price": 457.05}
    ]
    return render_template("stocks.html", data=stocks)