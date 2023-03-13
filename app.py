from tkinter import Button
from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)

app.secret_key = "asdfghjkl789456123"

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
        
    if "attempts" not in session:
        session['attempts'] = 0
        print("Initialize in zero attempts")
    else:
        pass
    return render_template("index.html")

@app.route('/guess', methods = ['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    
    if request.form.get('guess_number') == 'Guess Number':
        session["attempts"] += 1
        print("Added one more try")        
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/winners', methods=['POST'])
def winners():
    session['name'] = request.form['name']
    return render_template("winners.html")

@app.route('/back')
def back_home():
    session.clear()
    return redirect('/')

# if __name__ == "__main__":
#    app.run(debug = True)
