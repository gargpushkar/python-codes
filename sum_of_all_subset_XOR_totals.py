# Sum of All Subset XOR Totals
# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

# Input: nums = [5,1,6]
# Output: 28
# Explanation: The 8 subsets of [5,1,6] are:
# - The empty subset has an XOR total of 0.
# - [5] has an XOR total of 5.
# - [1] has an XOR total of 1.
# - [6] has an XOR total of 6.
# - [5,1] has an XOR total of 5 XOR 1 = 4.
# - [5,6] has an XOR total of 5 XOR 6 = 3.
# - [1,6] has an XOR total of 1 XOR 6 = 7.
# - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
# 0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

# Input: nums = [3,4,5,6,7,8]
# Output: 480
# Explanation: The sum of all XOR totals for every subset is 480.

# nums = [5, 1, 6]
nums = [3,4,5,6,7,8]

def power_set(nums, output_list, ans):
    if len(nums) == 0:
        if output_list:
            xor = output_list[0]
            for i in range(1, len(output_list)):
                xor ^= output_list[i]
            ans[0] += xor
        return
    elem = nums[0]
    nums = nums[1:]
    without_elem = output_list[::]
    with_elem = output_list[::]
    with_elem.append(elem)
    power_set(nums, without_elem, ans)
    power_set(nums, with_elem, ans)
    return ans[0]

print(power_set(nums, [], [0]))