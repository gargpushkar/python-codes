# Number of occurrence
# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

# Example 1:
# Input:
# N = 7, X = 2
# Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 4
# Explanation: 2 occurs 4 times in the
# given array.

# Example 2:
# Input:
# N = 7, X = 4
# Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 0
# Explanation: 4 is not present in the
# given array.

class Solution:
    def count(self,arr, n, x):
        # code here
        l = 0
        r = n-1
        i = -1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                r = mid - 1
            else:
                i = mid
                r = mid - 1
        if i == -1:
            return 0
        l = 0
        r = n-1
        j = -1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                r = mid - 1
            else:
                j = mid
                l = mid + 1
        return j-i+1
