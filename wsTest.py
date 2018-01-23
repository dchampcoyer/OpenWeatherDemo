import requests
import json

api_key = "ecf0dcdfc655c8033a567fc40a459a09"

# Get the feed
r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=" + api_key)
r.text

# Convert it to a Python dictionary
data = json.loads(r.text)

print data
