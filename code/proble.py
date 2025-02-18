nums = [0,1,3,5]
dic = {}
lent = range(len(nums)+1)
for num in nums:
    if num not in dic:
        dic[num] = 1
for i in lent:
    if i not in dic:
        print(i)

x = "this is a string"

print(x[::-1])
_ = 10
print(_)
x, y = z = 1, 2
print (x, y, z)
