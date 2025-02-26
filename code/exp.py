# def longest_common_prefix(arr):
#     if not arr:  # If the array is empty, return an empty string
#         return ""
    
#     # Find the shortest string in the array
#     shortest = min(arr, key=len)
    
#     # Iterate through each character of the shortest string
#     for i, char in enumerate(shortest):
#         # Compare this character with the corresponding character in all other strings
#         for string in arr:
#             if string[i] != char:
#                 return shortest[:i]  # Return the prefix up to the mismatch
    
#     return shortest  # If no mismatch, return the entire shortest string

# # Example usage
# arr = ["fla", "flow", "flee"]
# result = longest_common_prefix(arr)
# print("Longest common prefix:", result)
# str = ["hello","wello"]

# stren = enumerate(str)
# print(stren)

# def count_last_word_letters(input_string):
#     count = 0  # Initialize the letter counter
#     i = len(input_string) - 1  # Start from the last index of the string

#     # Step 1: Skip trailing spaces
#     while i >= 0 and input_string[i] == " ":
#         i -= 1

#     # Step 2: Count letters until the first space is encountered
#     while i >= 0 and input_string[i] != " ":
#         count += 1
#         i -= 1

#     return count

# # Example usage
# input_string = "  hello world  "
# result = count_last_word_letters(input_string)
# print("Number of letters in the last word:", result)
# i,j = 1,2
# print(i,j)
# num = int(input("please enter a number:"))

# while num <= 100:
#     num*=2
#     print(num)
a = ["appple","guava"]
b = [x for x in a]
print(b)