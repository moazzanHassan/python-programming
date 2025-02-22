import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Get user input for URL, count, and position
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1  # Convert to zero-based index

print("Retrieving:", url)

# Loop through the process count times
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    links = soup('a')

    # Get the link at the specified position
    url = links[position].get('href', None)
    print("Retrieving:", url)

# Extract and print the last name from the final URL
name = url.split('_')[-1].split('.')[0]
print("The answer to the assignment is:", name)
