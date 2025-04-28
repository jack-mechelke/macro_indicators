# fetch_data.py
from fredapi import Fred
from config import FRED_API_KEY

fred = Fred(api_key=FRED_API_KEY)

def fetch_all_data():
    data = {
        "GDP Growth YoY (%)": fred.get_series('A191RL1Q225SBEA').iloc[-1],
        "Unemployment Rate (%)": fred.get_series('UNRATE').iloc[-1],
        "CPI Inflation YoY (%)": fred.get_series('CPIAUCSL').pct_change(12).dropna().iloc[-1]*100,
        "Industrial Production YoY (%)": fred.get_series('INDPRO').pct_change(12).dropna().iloc[-1]*100, # instead of ISM Manufacturing PMI
        "Initial Jobless Claims (k)": fred.get_series('ICSA').iloc[-1]/1000,
        "Fed Funds Rate (%)": fred.get_series('FEDFUNDS').iloc[-1],
    }
    return data

def fetch_historical_series(series_id, periods=40):
    return fred.get_series(series_id)[-periods:]

def fetch_historical_cpi(periods=40):
    series = fred.get_series('CPIAUCSL').pct_change(12).dropna()
    return series[-periods:] * 100