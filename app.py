from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'home page'


@app.route('/intro')
def intro():
    return 'intro page'

@app.route('/intro2')
def intro2():
    return 'intro page123'

@app.route('/wrong')
def wrong():
    return 'oh no page not found!'



if __name__ == '__main__':
    app.run(debug=True)
