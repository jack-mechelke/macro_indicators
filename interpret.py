# interpret.py

def interpret_gdp(gdp):
    if gdp > 2:
        return "Healthy growth ✅"
    elif 0 < gdp <= 2:
        return "Slowing ⚠️"
    else:
        return "Contraction 🚨"
    
def interpret_unemployment(rate):
    if rate > 4:
        return "Tight labor market ✅"
    elif 4 <= rate < 5:
        return "Softening labor ⚠️"
    else:
        return "Stress in jobs market 🚨"

def interpret_cpi(cpi):
    if cpi < 2.5:
        return "Inflation under control ✅"
    elif 2.5 <= cpi < 4:
        return "Moderate inflation ⚠️"
    else:
        return "High inflation 🚨"

def interpret_ism(pmi):
    if pmi > 50:
        return "Expansion ✅"
    elif 47 <= pmi <= 50:
        return "Near stall speed ⚠️"
    else:
        return "Contraction 🚨"

def interpret_jobless_claims(claims):
    if claims < 250:
        return "Labor market stable ✅"
    elif 250 <= claims <= 300:
        return "Softening ⚠️"
    else:
        return "Layoffs accelerating 🚨"

def interpret_fed_rate(rate):
    if rate < 2:
        return "Loose policy ✅"
    elif 2 <= rate <= 5:
        return "Moderate policy ⚠️"
    else:
        return "Tight conditions 🚨"

def interpret_esi(esi):
    if esi > 0:
        return "Positive surprises ✅"
    elif -50 < esi <= 0:
        return "Mixed data ⚠️"
    else:
        return "Negative surprises 🚨"

def interpret_vix(vix):
    if vix < 15:
        return "Calm market ✅"
    elif 15 <= vix <= 25:
        return "Moderate volatility ⚠️"
    else:
        return "High fear 🚨"

def interpret_all(data):
    return {
        "GDP Growth YoY (%)": interpret_gdp(data["GDP Growth YoY (%)"]),
        "Unemployment Rate (%)": interpret_unemployment(data["Unemployment Rate (%)"]),
        "CPI Inflation YoY (%)": interpret_cpi(data["CPI Inflation YoY (%)"]),
        "Industrial Production YoY (%)": interpret_ism(data["Industrial Production YoY (%)"]),  # Use ISM-style logic temporarily
        "Initial Jobless Claims (k)": interpret_jobless_claims(data["Initial Jobless Claims (k)"]),
        "Fed Funds Rate (%)": interpret_fed_rate(data["Fed Funds Rate (%)"]),
    }