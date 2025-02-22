import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input("Enter location: ")
print("Retrieving", url)

# Read data from the URL
data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

# Parse XML
tree = ET.fromstring(data)

# Extract all 'count' elements
counts = tree.findall('.//count')

# Convert text to integers and compute the sum
sum_counts = sum(int(count.text) for count in counts)

# Print results
print("Count:", len(counts))
print("Sum:", sum_counts)
