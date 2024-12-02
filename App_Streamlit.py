import streamlit as st
import joblib
import pandas as pd
from prophet.plot import plot_plotly

model = joblib.load('modelo\modelo_prophet.pkl')

st.title("Previsão do Preço do Petróleo Brent")

days = st.number_input("Quantos dias para previsão?", min_value=1, max_value=365, value=7)

last_date = pd.Timestamp("2024-11-18") 
model.history['ds'] = model.history['ds'] + (last_date - model.history['ds'].max())
future_dates = model.make_future_dataframe(periods=days)

forecast = model.predict(future_dates)

st.write("Previsão do preço em USD para os próximos {} dias:".format(days))
st.write(forecast[['ds', 'yhat']].tail(days))

plot = plot_plotly(model, forecast)
st.plotly_chart(plot)