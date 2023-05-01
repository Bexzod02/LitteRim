from geopy.geocoders import Nominatim

def manzil(latitude, longitude):
    geolocator = Nominatim(user_agent='Bexzod')
    location = geolocator.reverse(f'{latitude},{longitude}')
    return location.address