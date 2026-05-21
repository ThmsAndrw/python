from flask import Flask, render_template

app = Flask(__name__)

@aoo.route('/')
def home():
    return render_template('home.html')

@aoo.route('/page2')
def home():
    return render_template('page2.html')

@aoo.route('/page3')
def home():
    return render_template('page3.html')

@aoo.route('/page4')
def home():
    return render_template('page4.html')

if __name__ == '__main__':
    app.run(debug=True)