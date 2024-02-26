# Brute Force    -- n*n
# arr = [1, 3, 2, 4, 1, 6, 5, 7, 3, 4, 5, 6, 10, 4, 3, 20]
arr = [100, 80, 60, 70, 60, 75, 85]
# arr = [1, 3, 0, 7, 8, 5, 4]
n = len(arr)

ans = [-1]
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if arr[j] > arr[i]:
            ans.append(arr[j])
            break
        if j == 0:
            ans.append(-1)

print(ans)
# Using Stack
# 3 conditions to check
# if stack is empty, push -1 in the answer................ push current_element onto the stack
# if stack.top is greater than current element, push stack.top in ans................ push current_element onto the stack
# is stack.top is less than current element, pop stack untill it becomes empty or stack.top becomes greater than current element................ push current_element onto the stack


stack = []
ans = []
for i in range(n):
    if not stack:
        ans.append(-1)
    else:
        if stack[-1] > arr[i]:
            ans.append(stack[-1])
        else:
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
    stack.append(arr[i])

print(ans)


# Another way of writing above code
stack = []
ans = []
for i in range(n):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(arr[i])
print(ans)