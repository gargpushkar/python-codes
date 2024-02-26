# Unsolved Incorrect

# https://www.geeksforgeeks.org/problems/peak-element/1?page=2&sortBy=submissions
# Peak element
# Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist). The array is guaranteed to be in ascending order before the peak element and in descending order after it.

# Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

# Example 1:

# Input: 
# n = 3
# arr[] = {1, 2, 3}
# Peak Element's Index: 2
# Output: 1
# Explanation: 
# If the index returned is 2, then the output printed will be 1. 
# Since arr[2] = 3 is greater than its adjacent elements, and 
# there is no element after it, we can consider it as a peak 
# element. No other index satisfies the same property.
# Example 2:

# Input:
# n = 3
# arr[] = {3, 4, 2}
# Peak Element's Index: 1
# Output: 1
# Explanation: 
# If the index returned is 1, then the output printed will be 1.
# Since arr[1] = 4 is greater than its adjacent elements, and
# there is no element after it, we can consider it as a peak
# element. No other index satisfies the same property.

# arr = [1, 2, 3, 4, 5, 6, 2, 3]
# arr = [59, 73, 13, 53, 26, 77, 46, 29, 3, 86, 34, 49]
# arr = [1, 2, 3]
# arr = [3]

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)

i = 0
j = n-1
elem = 9

while(i<=j):
    mid = (i+j)//2
    if arr[mid] == elem:
        print(True)
        print(arr[mid])
        break
    if arr[mid] > elem:
        j = mid-1
    else:
        i = mid + 1

    # if arr[mid-1] < arr[mid]  and arr[mid] > arr[mid+1]:
    #     print(mid)
    #     break
    # if arr[mid-1] < arr[mid] and arr[mid] < arr[mid+1]:
    #     i = mid + 1
    # else:
    #     j = mid - 1
