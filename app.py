from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
from services.exchange_rate_service import get_currencies_last_month, get_currencies_from_res, compare_currencies_period

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'fl@$k'

time_period_list = ['1 week', '2 weeks', '3 weeks', '4 weeks']

# Form Class
class CurrencyExchangeForm(Form):
    target_currency = StringField('Target Currency', [validators.DataRequired()])
    base_currency = StringField('Base Currency', [validators.DataRequired()])
    time_period = StringField('Time Period', [validators.DataRequired()])

@app.route('/', methods=['GET'])
def currency_chart():
    """
        Get currency data for the last month
        :param url: None
        :returns: Template
    """
    
    # Get Data
    data = get_currencies_last_month()
    currencies = get_currencies_from_res(data)
    return render_template('index.html', data=data, currencies=currencies, time_period_list=time_period_list)

@app.route('/submit', methods=['POST'])
def currency_compare():
    """
        Get currency data for the required currencies for the required time period
        :param url: None
        :returns: Template
    """
    
    # Init Form controls
    form = CurrencyExchangeForm(request.form)
    
    target_curr = request.form['target_currency']
    base_curr = request.form['base_currency']
    time_per = int(request.form['time_period'][0])
    
    # Get Data
    data = compare_currencies_period(target_curr, base_curr, time_per)
    currencies = get_currencies_from_res(get_currencies_last_month())
    return render_template('index.html', data=data, currencies=currencies, time_period_list=time_period_list)