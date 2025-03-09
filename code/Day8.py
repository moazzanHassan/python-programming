def findDifference(s,t):
    for char in t:
        count_s = s.count(char)
        count_t = t.count(char)
    if count_s!=count_t:
        return char

print(findDifference('abcd','abcde'))