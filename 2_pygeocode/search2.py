#!/usr/bin/env python3
import requests
from geopy.geocoders import Nominatim

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one=False, limit=3, addressdetails=True)
    cep1: str = location[0].raw['address']['postcode']
    cep2: str = location[1].raw['address']['postcode']
    print("Endereço buscado", address, "\nResultado 1: \n CEP: ", cep1, "\nLatitude e Longitude: ",
          reply[0]["lat"], reply[0]["lon"], "\nCEP: ", cep2, "\nLatitude e Longitude: ",
          reply[1]["lat"], reply[1]["lon"])


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')