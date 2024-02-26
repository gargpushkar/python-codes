# Asteroid Collision
# We are given an integer array asteroids of size N representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are of same size, both will explode. Two asteroids moving in the same direction will never meet.
 

# Example 1:

# Input:
# N = 3
# asteroids[ ] = {3, 5, -3}
# Output: {3, 5}
# Explanation: The asteroid 5 and -3 collide resulting in 5. The 5 and 3 never collide.
# Example 2:

# Input:
# N = 2
# asteroids[ ] = {10, -10}
# Output: { }
# Explanation: The asteroid -10 and 10 collide exploding each other.

from collections import deque

arr = [3, 5,  -3]
arr = [10, -10]
arr = [-6, 5, 3, 5,  -3, -2, -1, -4]
arr = [-6, -5, 5, 2, 6, 1, 1, -2, 7]
arr = [-5, 5, 2, 1, 1, -2]
n = len(arr)
stack = deque()

def is_same_set(num1, num2):
    if num1 < 0 and num2 < 0:
        return True
    if num1 > 0 and num2 > 0:
        return True
    return False

for i in range(n-1, -1, -1):
    if not stack or arr[i] < 0:
        stack.append(arr[i])
    else:
        if is_same_set(stack[-1], arr[i]):
            stack.append(arr[i])
        else:
            while stack and not is_same_set(stack[-1], arr[i]):
                if abs(stack[-1]) < abs(arr[i]):
                    stack.pop()
                else:
                    break
            if stack and not is_same_set(stack[-1], arr[i]):
                if abs(stack[-1]) == abs(arr[i]):
                    stack.pop()
            else:
                stack.append(arr[i])
    
print(list(stack)[::-1])