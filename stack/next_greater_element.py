# Next Greater Element
# Given an array of positive integers A, find the first greater number for every element on its right. If a greater number does not exist, use -1.

# Example:
# Input: [1, 5, 2, 3, 5]
# Output: [5, -1, 3, 5, -1]


arr = [1, 5, 2, 3, 5]
stack = []
ans = []
for i in range(len(arr)-1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(arr[i])

print(ans[::-1])