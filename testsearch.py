from urllib.request import urlopen
import json

locu_api ="S8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe"
html = urlopen("https://api.locu.com/v1_0/venue/search/?country=UNITED%20STATES&locality=Washington&category=restaurant&api_key=8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe")
data =json.loads(html.read())
print(data['objects'])
		










