from flask import Flask
from flask import render_template, request, redirect, url_for
from block import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['lender']
        amount = request.form['amount']
        to_whom = request.form['borrower']
        write_block(name=name, amount=amount, to_whom=to_whom)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)