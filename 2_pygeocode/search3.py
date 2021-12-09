#!/usr/bin/env python3
import http.client
import json
from urllib.parse import quote_plus
from geopy.geocoders import Nominatim

base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Search3.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one=False, limit=3, addressdetails=True)
    cep1: str = location[0].raw['address']['postcode']
    cep2: str = location[1].raw['address']['postcode']
    print("Endereço buscado", address, "\nResultado 1: \n CEP: ", cep1, "\nLatitude e Longitude: ",
          reply[0]["lat"], reply[0]["lon"], "\nCEP: ", cep2, "\nLatitude e Longitude: ",
          reply[1]["lat"], reply[1]["lon"])

if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')