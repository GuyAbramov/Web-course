from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'


@app.route('/intro')
def intro():
    return 'intro page'

@app.route('/intro2')
def intro2():
    return 'oh no the page is not ready'

@app.route('/google')
def wrong():
    return 'google time'


if __name__ == '__main__':
    app.run(debug=True)
