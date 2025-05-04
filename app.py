from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
money = 100
a = 1
cost = 100

@app.route('/', methods = ['POST', 'GET'])
def main():
    global money
    global cost
    if request.method == 'POST':
        money += a
        return redirect('/')
    else:
        return render_template('index.html', money=money)

@app.route('/shop', methods = ['POST', 'GET'])
def shop():
    global money
    global cost
    global a
    if request.method == 'POST':
        if money >= cost:
            money -= cost
            a *= 2
            cost *= 2.5
            cost = int(cost)
            return redirect('/shop')
        else:
            return """
            <p>Недостаточно денег!</p>
            <a href="/"><h2>Домой</h2></a>
            """
    else:
        return render_template('shop.html', money=money, cost=cost)

if __name__ == '__main__':
    app.run(debug=True)
