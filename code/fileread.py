import re

# Open the file and read its content
with open("regex_sum_2160458.txt", "r") as file:
    data = file.read()

# Extract numbers using regex
numbers = re.findall(r'\d+', data)

# Convert extracted numbers to integers and calculate sum
total_sum = sum(map(int, numbers))

print("Sum:", total_sum)
