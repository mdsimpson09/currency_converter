# main flask app

from flask import Flask, render_template, request, jsonify, session, redirect
import requests 
from currency_converter import validate_currency_code, validate_amount, convert_currency

from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        # Retrieve user input from the form
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        # Validate currency codes and amount
        if validate_currency_code(from_currency) and validate_currency_code(to_currency) and validate_amount(amount):
            # Perform currency conversion using forex-python module
            result = convert_currency(from_currency, to_currency, float(amount))
            return render_template('result.html', result=result)
        else:
            error_message = "Invalid currency code or amount."
            return render_template('error.html', error_message=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         from_currency = request.form['from_currency']
#         to_currency = request.form['to_currency']
#         amount = request.form['amount']

#         if not is_valid_currency_code(from_currency):
#             error_message = f"Invalid currency code: {from_currency}"
#             return render_template('index.html', error_message=error_message)
#         if not is_valid_currency_code(to_currency):
#             error_message = f"Invalid currency code: {to_currency}"
#             return render_template('index.html', error_message=error_message)
#         try:
#             amount = float(amount)
#         except ValueError:
#             error_message = "Invalid amount entered"
#             return render_template('index.html', error_message=error_message)

#         converted_amount = convert_currency(from_currency, to_currency, amount)
#         return render_template('index.html', converted_amount=converted_amount)

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()

