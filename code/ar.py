nums = [1,2,3,3,6]
val = 3
k = 0  # Pointer to track the position of non-val elements

for i in range(len(nums)):
    if nums[i] != val:  # Keep elements that are not equal to val
        nums[k] = nums[i]  # Overwrite at index k
        k += 1  # Move k forward

print(k) 