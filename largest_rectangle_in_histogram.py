# https://workat.tech/problem-solving/practice/largest-rectangle-histogram
# You are given a list of non-negative integers denoting the bar heights of a histogram. All the bars have a width of 1. You need to find the area of the largest possible rectange in the histogram.

#       [-1,-1, 1,  2, 1,-1,  5, 5 ]
# arr = [8, 2, 10, 12, 7, 0, 10, 8]
#       [1, 5, 4, 4, 5, 8, 7, 8]
#       [0, 1, 2,   3, 4, 5,  6, 7]
# ans = 21

# arr = [8, 2, 10, 12, 7, 0, 10, 8]
arr = [1, 3, 2]
n = len(arr)
nearest_smaller_left_stack = []
array_left = []
nearest_smaller_right_stack = []
array_right = []

for i in range(n):
    while(nearest_smaller_left_stack and nearest_smaller_left_stack[-1][0] >= arr[i]):
        nearest_smaller_left_stack.pop()
    if nearest_smaller_left_stack:
        array_left.append(nearest_smaller_left_stack[-1][1])
    else:
        array_left.append(-1)    
    nearest_smaller_left_stack.append((arr[i], i))

for i in range(n -1, -1, -1):
    while(nearest_smaller_right_stack and nearest_smaller_right_stack[-1][0] >= arr[i]):
        nearest_smaller_right_stack.pop()
    if nearest_smaller_right_stack:
        array_right.append(nearest_smaller_right_stack[-1][1])
    else:
        array_right.append(n)
    nearest_smaller_right_stack.append([arr[i], i])
array_right = array_right[::-1]

width_array = []
for i in range(n):
    width_array.append(array_right[i] - array_left[i] - 1)

ans = []
for i in range(n):
    ans.append(width_array[i] * arr[i])
print(max(ans))