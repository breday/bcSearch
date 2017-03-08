from urllib.request import urlopen
import json

locu_api = "8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe"
url = 'https://api.locu.com/v1_0/venue/search/?country=UNITED%20STATES&locality=Washington&category=restaurant&api_key=8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe'
url = urlopen('https://api.locu.com/v1_0/venue/search/?country=UNITED%20STATES&locality=Washington&category=restaurant&api_key=8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe')
json_obj = urllib.urlopen(url)
data = json.loads(json_obj)

url = urlopen("https://api.locu.com/v1_0/venue/search/?country=%s" %name)
@data= url.read().decode('utf')

data = json.load(json_obj)
json_obj = json.loads(data)
#data1 = json.dumps(data)
print(json_obj)
# print (json.loads(json_obj),['objects'])

#for item in data['objects']:
	#if query =="yes":https://api.locu.com/v1_0/venue/search/?country=united%20states&locality=washington&category=restaurant&api_key=8c0fdafa35e5ce90c36ede4ee4184bdc40b9f6fe
		#print (item['"name"'])
	#else:
		#print (None)
