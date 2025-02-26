import urllib.request
import json

# Prompt for URL
url = input("Enter location: ")
print("Retrieving", url)

# Open the URL and read the data
response = urllib.request.urlopen(url)
data = response.read().decode()
print("Retrieved", len(data), "characters")

# Parse JSON
json_data = json.loads(data)

# Extract comment counts and compute the sum
total = sum(item["count"] for item in json_data["comments"])

# Print results
print("Count:", len(json_data["comments"]))
print("Sum:", total)
