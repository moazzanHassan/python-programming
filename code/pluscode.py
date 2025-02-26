import urllib.parse
import urllib.request
import json

# API endpoint
service_url = "http://py4e-data.dr-chuck.net/opengeo?"

# Get user input for location
location = input("Enter location: ")
print("Retrieving", location)

# Encode parameters
params = {"q": location}
url = service_url + urllib.parse.urlencode(params)

print("Retrieving", url)

# Fetch data from URL
response = urllib.request.urlopen(url)
data = response.read().decode()

print("Retrieved", len(data), "characters")

# Parse JSON data
try:
    js = json.loads(data)
except json.JSONDecodeError:
    print("Failed to parse JSON")
    exit()

# Extract plus_code if available
try:
    plus_code = js["features"][0]["properties"]["plus_code"]
    print("Plus code:", plus_code)
except (KeyError, IndexError):
    print("No plus code found")
