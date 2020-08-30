import requests
from datetime import *
from dateutil.relativedelta import *

# Constants
base_url = 'https://api.exchangeratesapi.io/'
month_offset = 1
date_string_format = '%Y-%m-%d'
today = date.today()

def get_currencies_from_res(res):
    """
        Get list of all currencies
        :param value: Response of the API
        :returns: List of Currencies
    """
    
    key = list(res.keys())[0]
    return list(res[key].keys())

def get_currencies_last_month():
    """
        Get currency data for the last month
        :param value: None
        :returns: Response
    """
    
    api_type = 'history?'
    start_at = today-relativedelta(months=month_offset)
    end_at = today.strftime(date_string_format)
    # Building URL
    req_url = base_url + api_type + 'start_at=' + start_at.strftime(date_string_format) + '&end_at=' + end_at
    return requests.get(req_url).json()['rates']

def compare_currencies_period(target_curr, base_curr, time_per):
    """
        Get currency data for the required currencies for the required time period
        :param value target_curr, base_curr, time_per: Target Currency, Base Currency & Time Period
        :returns: Response
    """
    
    api_type = 'history?'
    start_at = today-relativedelta(weeks=time_per)
    end_at = today.strftime(date_string_format)
    # Building URL
    req_url = base_url + api_type + 'start_at=' + start_at.strftime(date_string_format) + '&end_at=' + end_at + '&symbols=' + target_curr + '&base=' + base_curr
    return requests.get(req_url).json()['rates']
    
    