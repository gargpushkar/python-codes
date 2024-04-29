# Swap Sort

nums = [1,3,4,2,2, 5, 6, 3, 5, 3, 9]

n = len(nums)

i = 0
while i < n:
    correct_pos = nums[i] - 1
    if nums[i] != nums[correct_pos]:
        nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
    else:        # either duplicate or already in the correct position
        i+=1

print(nums)

missing = []
duplicate = []
for i in range(n):
    if i+1 != nums[i]:
        missing.append(i+1)
        duplicate.append(nums[i])

print(missing)
print(duplicate)