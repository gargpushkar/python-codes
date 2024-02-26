# Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
# Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
# If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

# Example 1:

# Input: 
# N = 4, arr[] = [1 3 2 4]
# Output:
# 3 4 4 -1
# Explanation:
# In the array, the next larger element 
# to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
# since it doesn't exist, it is -1.

# Brute Force    -- n*n
# arr = [1, 3, 2, 4]
# arr = [6, 8, 0, 1, 3]
arr = [1, 3, 0, 0, 1, 2, 4]
n = len(arr)
ans = []
for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            ans.append(arr[j])
            break
        if j == n-1:
            ans.append(-1)
ans.append(-1)
print(ans)

# Using Stack
stack = []
ans = []
for i in range(len(arr)-1, -1, -1):
    if not stack:
        ans.append(-1)
    else:
        if stack[-1] > arr[i]:
            ans.append(stack[-1])
            stack.append(arr[i])
        else:
            while(stack and stack[-1] <= arr[i]):
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
    stack.append(arr[i])
print(ans[::-1])