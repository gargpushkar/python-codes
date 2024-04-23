# Bitonic Point
# Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.
# Note: If the array is increasing then just print the last element will be the maximum value.

# Example 1:
# Input: 
# n = 9
# arr[] = {1,15,25,45,42,21,17,12,11}
# Output: 45
# Explanation: Maximum element is 45.

# Example 2:
# Input: 
# n = 5
# arr[] = {1, 45, 47, 50, 5}
# Output: 50
# Explanation: Maximum element is 50.

arr = [1, 15, 25, 45, 42, 21, 17, 12, 11]
arr = [1, 45, 47, 50, 5]
arr = [1, 45, 47, 50]
arr = [5, 4, 3, 2, 1]
arr = [5]
n = len(arr)

def findMaximum(arr, n):
    l = 0
    r = n - 1
    if n == 1:
        return arr[-1]
    while l <= r:
        mid = l + (r-l)//2
        if mid > 0 and mid < n-1:
            if arr[mid] > arr[mid-1] and arr[mid] >  arr[mid+1]:
                return arr[mid]
            elif arr[mid] > arr[mid-1]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if mid == 0:
                if arr[mid] > arr[mid+1]:
                    return arr[mid]
                else:
                    return arr[mid+1]
            else:
                if arr[mid] > arr[mid-1]:
                    return arr[mid]
                else:
                    return arr[mid-1]


print(findMaximum(arr, n))
