# app.py
import streamlit as st
from fetch_data import fetch_all_data, fetch_historical_series, fetch_historical_cpi
from interpret import interpret_all

st.set_page_config(page_title="Macro Dashboard", layout="wide")

# Fetch latest data
data = fetch_all_data()

# Interpret data
interpretations = interpret_all(data)

# Display
st.title("Macro Dashboard")

cols = st.columns(3)

def color_text(text):
    if "✅" in text:
        color = "green"
    elif "⚠️" in text:
        color = "orange"
    elif "🚨" in text:
        color = "red"
    else:
        color = "gray"
    return f"<span style='color:{color}'>{text}</span>"

for idx, (indicator, value) in enumerate(data.items()):
    with cols[idx % 3]:
        st.metric(label=indicator, value=f"{value:.2f}")
        st.markdown(color_text(interpretations[indicator]), unsafe_allow_html=True)

st.header("Historical Trends")

col1, col2 = st.columns(2)

with col1:
    st.subheader("GDP Growth YoY (%)")
    gdp_series = fetch_historical_series('A191RL1Q225SBEA')
    st.line_chart(gdp_series)

with col2:
    st.subheader("Unemployment (%)")
    unemployment_series = fetch_historical_series('UNRATE')
    st.line_chart(unemployment_series)

col3, col4 = st.columns(2)

with col3:
    st.subheader("CPI Inflation YoY (%)")
    cpi_series = fetch_historical_cpi()
    st.line_chart(cpi_series)

with col4:
    st.subheader("Fed Funds Rate (%)")
    fedfunds_series = fetch_historical_series('FEDFUNDS')
    st.line_chart(fedfunds_series)
