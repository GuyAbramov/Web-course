from flask import Flask ,redirect ,url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'


@app.route('/intro')
def intro():
    #problem
    return redirect('/intro2')

@app.route('/intro2')
def intro2():
    return 'oh no the page is not ready'

@app.route('/google')
def google():
    return redirect(url_for('moogle'))

@app.route('/moogle')
def moogle():
    return 'moogle time'



if __name__ == '__main__':
    app.run(debug=True)
