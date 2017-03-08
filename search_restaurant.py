import urllib
import json

locu_api = S8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe
url =('https://api.locu.com/v1_0/venue/search/?country=UNITED%20STATES&locality=Washington&category=restaurant&api_key=8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe')
json_obj = urllib.urlopen(url)
data = json.load(json_obj)



restaurant = input(Do you want to see all restaurants found around the  washington area?)
for item in data['objects']:
	if restaurant =="yes":
		return item['name']
	else:
		return None
		

















	

