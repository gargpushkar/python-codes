# Rotation
# Given an ascending sorted rotated array arr of distinct integers of size n. The array is right-rotated k times. Find the value of k.

# Example 1:
# Input:
# n = 5
# arr[] = {5, 1, 2, 3, 4}
# Output: 1
# Explanation: The given array is 5 1 2 3 4. 
# The original sorted array is 1 2 3 4 5. 
# We can see that the array was rotated 
# 1 times to the right.

# Example 2:
# Input:
# n = 5
# arr[] = {1, 2, 3, 4, 5}
# Output: 0
# Explanation: The given array is not rotated.

arr = [5, 6, 7, 8, 1, 2, 3, 4]
# arr = [66, 72, 79, 86, 95, 104, 106, 110, 119, 123, 124, 129, 132, 136, 137, 142, 150, 2, 12, 14, 17, 26, 30, 36, 38, 46, 52, 60]
n = len(arr)

def rotate(arr, n):
    l = 0
    r = n - 1
    if arr[l] <= arr[r]:
        return 0
    
    while l<r:
        mid = l + (r-l)//2
        if arr[mid] >= arr[0]:
            l = mid + 1
        else:
            r = mid
    return l

print(rotate(arr, n))