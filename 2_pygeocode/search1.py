#!/usr/bin/env pytho3

from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one=False, limit=3, addressdetails=True)
    cep1: str = location[0].raw['address']['postcode']
    cep2: str = location[1].raw['address']['postcode']
    print("Endereço buscado", address, "\nResultado 1: \n CEP: ", cep1, "\nLatitude e Longitude: ",
          location[1].latitude, location[1].longitude, "\nCEP: ", cep2, "\nLatitude e Longitude: ",
          location[0].latitude, location[0].longitude)
