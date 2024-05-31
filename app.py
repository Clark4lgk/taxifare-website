import streamlit as st
import requests
import datetime

# Title of the app
st.title("TaxiFareModel Frontend")

# Markdown text
st.markdown('''
## Welcome to the Taxi Fare Prediction App!
Use this app to get a prediction of taxi fares in New York City.
''')

# Input fields for the ride parameters
st.header("Enter the ride details")

# Date and time
pickup_date = st.date_input("Pickup date", datetime.date.today())
pickup_time = st.time_input("Pickup time", datetime.datetime.now().time())

# Pickup longitude and latitude
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)

# Dropoff longitude and latitude
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

# Passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

# Call the API
if st.button("Get Fare Prediction"):
    # Create a dictionary with the parameters
    params = {
        "pickup_datetime": f"{pickup_date} {pickup_time}",
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # URL of the API
    url = 'https://taxifare.lewagon.ai/predict'

    # Make the API request
    response = requests.get(url, params=params)
    prediction = response.json()

    # Display the prediction
    st.write(f"Predicted Fare: ${prediction['fare_amount']:.2f}")

# Optional: Add a map to show the pickup and dropoff points
st.header("Ride Map")
st.map({
    "lat": [pickup_latitude, dropoff_latitude],
    "lon": [pickup_longitude, dropoff_longitude]
})
