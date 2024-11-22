import streamlit as st
import requests
import datetime 
'''
# TaxiFareModel front
'''


with st.form(key="api_parameters"):
    date = st.date_input('date')
    time=st.time_input('time')
    pickup_long = st.number_input('pickup_longitude',format="%0.6f")
    pickup_lat=st.number_input('pickup_latitude',format="%0.6f")
    dropoff_long=st.number_input('dropoff_longitude',format="%0.6f")
    dropoff_lat=st.number_input('dropoff_latitude',format="%0.6f")
    passenger_count = st.number_input("Passenger_count", min_value=1, max_value=10, step=1)
    st.form_submit_button('upload')

date_time=f'{date} {time}'
# st.write(date)
# st.write(time)
# st.write(pickup_long)
# st.write(pickup_lat)
# st.write(dropoff_long)
# st.write(dropoff_lat)
# st.write(passenger_count)

url = 'https://taxifare.lewagon.ai/predict'

params={
'pickup_datetime': date_time,
'pickup_longitude':pickup_long,
'pickup_latitude': pickup_lat,
'dropoff_longitude': dropoff_long,
'dropoff_latitude': dropoff_lat,
'passenger_count':passenger_count
}

print (date)
print(time)
response=requests.get(url=url,params=params).json()['fare']
st.markdown('Taxi fare $')
st.write(response)