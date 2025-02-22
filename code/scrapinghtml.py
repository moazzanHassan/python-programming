import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Enter the actual URL provided in the assignment
url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
tags = soup("span")
numbers = [int(tag.text) for tag in tags]

# Compute the sum
print("Sum:", sum(numbers))
