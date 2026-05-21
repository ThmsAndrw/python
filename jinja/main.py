from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/q1')
def q1():
    name = "João"
    
    return render_template('q1.html', name=name)

@app.route('/q2')
def q2():
    name = "João"
    age = 30
    
    return render_template('q2.html', name=name, age=age)

@app.route('/q3')
def q3():
    data = {
        'Nome': "Ana",
        'Email': "ana@email.com"
    }
    
    return render_template('q3.html', data=data)

@app.route('/q4')
def q4():
    nameList = ["Thomas", "Vitinho", "André", "Coxão", "Anteta", "Luan"]
    
    return render_template('q4.html', nameList=nameList)

@app.route('/q5')
def q5():
    data = {
        'Thomas': "9",
        'Victor': "3",
        'Andrew': "7",
        'Coxão': "10",
    }
    
    return render_template('q5.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)