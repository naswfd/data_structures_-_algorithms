import urllib.parse
import requests

address = 'ewr'
main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
url = main_api + urllib.parse.urlencode({'address': address})
json_data = requests.get(url).json()
json_status = json_data['status']
print('API status:' + json_status)
print(url)
formatted_address = json_data['results'][0]['formatted_address']
print(formatted_address)
