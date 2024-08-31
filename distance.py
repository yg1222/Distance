import requests
import json
import math
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

url = f'https://www.mapquestapi.com/directions/v2/routematrix?key={api_key}'

origin =input("Origin (zip/postal code, address, etc): ")
destination =input("Destination (zip/postal code, address, etc): ")
# origin='T3G5N4'
# destination='T2B3K1'
'''

'''
headers={'Content-Type': 'application/json'}
params = {'key':api_key, }
body={
    'locations': [
        origin, destination
    ],
    'units': 'm'
}

response = requests.post(url, headers=headers, json=body)
distance = response.json()['distance'][1]
seconds = response.json()['time'][1]
origin_obj = response.json()['locations'][0]
destination_obj = response.json()['locations'][1]
disp = f"\nThe distance between the {origin_obj['adminArea6']} {origin_obj['adminArea6Type']} in {origin_obj['adminArea5']} {origin_obj['adminArea3']} to the {destination_obj['adminArea6']} {destination_obj['adminArea6Type']} in {destination_obj['adminArea5']} {destination_obj['adminArea3']} is about {distance} kilometers and a drive time of about {math.ceil(seconds/60)} minutes."
print(disp)