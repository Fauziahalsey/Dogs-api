import requests
import json 

url = "https://dog.ceo/api/breeds/image/random" 
response = requests.get(url)
print (response.content)
json_content = json.loads(response.text)
print(json.dumps(json_content, indent=4, sort_keys=True))

json.loads(response.content)