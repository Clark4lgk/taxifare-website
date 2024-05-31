import streamlit as st
import requests
import datetime

# Titre de l'application
st.title("Façade du modèle TaxiFare")

# Introduction
st.markdown('''
# TaxiFareModel front

N'oubliez pas qu'il existe plusieurs façons d'afficher du contenu sur votre page Web...

Soit comme pour le titre en créant simplement une chaîne (ou une f-string). Ou comme avec ce paragraphe en utilisant les `st.` fonctions
''')

# Controles pour demander les paramètres du trajet
st.markdown('''
## Ici, nous aimerions ajouter quelques contrôleurs afin de demander à l'utilisateur de sélectionner les paramètres du trajet
Demandons :
- date et l'heure
- longitude de prise en charge
- latitude de prise en charge
- longitude de dépôt
- latitude de dépôt
- nombre de passagers
''')

# Input fields for the ride parameters
st.header("Entrez les détails du trajet")

# Date et heure
pickup_date = st.date_input("Date de prise en charge", datetime.date.today())
pickup_time = st.time_input("Heure de prise en charge", datetime.datetime.now().time())

# Longitude et latitude de prise en charge
pickup_longitude = st.number_input("Longitude de prise en charge", value=-73.985428)
pickup_latitude = st.number_input("Latitude de prise en charge", value=40.748817)

# Longitude et latitude de dépôt
dropoff_longitude = st.number_input("Longitude de dépôt", value=-73.985428)
dropoff_latitude = st.number_input("Latitude de dépôt", value=40.748817)

# Nombre de passagers
passenger_count = st.number_input("Nombre de passagers", min_value=1, max_value=8, value=1)

# Appeler l'API
if st.button("Obtenir la prédiction du tarif"):
    # Créer un dictionnaire avec les paramètres
    params = {
        "pickup_datetime": f"{pickup_date} {pickup_time}",
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # URL de l'API
    url = 'https://taxifare.lewagon.ai/predict'

    # Faire la requête à l'API
    response = requests.get(url, params=params)
    data = response.json()

    # Afficher la réponse brute pour le débogage
    st.write("Réponse de l'API : ", data)

