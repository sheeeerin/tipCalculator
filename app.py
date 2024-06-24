from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        total = float(request.form['total'])
        tip = int(request.form['tip'])
        people = int(request.form['people'])
        
        amount = total + (tip / 100 * total)
        each_amount = round(amount / people, 2)
        
        return render_template('result.html', each_amount=each_amount)
    except ValueError:
        return "Invalid input. Please enter numerical values for bill, tip, and people."

if __name__ == '__main__':
    app.run(debug=True)
