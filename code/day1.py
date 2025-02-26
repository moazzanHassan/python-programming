# num = [2,3,5,6]
# for i in range(len(num)):
#     print(i)
def main():
    dictionary = {}
    dictionary["learning"] = "awesome"
    dictionary["coding"] = "fun"
    # ... Fill with more data
    remove_keys_containing_string(dictionary, "learn")

"""
This Python function takes in a dict and a string and  
removes all keys containing that string from the dict
"""
# def remove_keys_containing_string(dictionary, remove):
#     new_dictionary = {}
#     for key in dictionary:
#         if remove not in key:
#             new_dictionary[key] = dictionary[key]
# def prit(n):
#     if n <=0:
#         return False
#     while n%2 == 0:
#         n = n/2
#     return n==1
# print(prit(1))
# li = {
#     "hello",
#     "hello"
# }
# print(li)
li = {"hello","ballo"}

print(li.pop())