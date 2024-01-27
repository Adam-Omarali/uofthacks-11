import requests

url = "https://shazam.p.rapidapi.com/search"

querystring = {"term":"happy music","locale":"en-US","offset":"0","limit":"5"}

headers = {
	"X-RapidAPI-Key": "0527e26709msh131b0dddef3f157p10ccf1jsnd4ac90309727",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())