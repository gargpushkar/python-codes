# Segregate 0s and 1s
# Given an array of length N consisting of only 0s and 1s in random order. Modify the array to segregate 0s on left side and 1s on the right side of the array.

# Example 1:

# Input:
# N = 5
# arr[] = {0, 0, 1, 1, 0}
# Output: 0 0 0 1 1

arr = [0, 0, 1, 1, 0]
n = 5

l, r = 0, n-1

while(l<r):
    if arr[l] == 1:
        if arr[r] != 1:
            arr[r], arr[l] = arr[l], arr[r]
        r-=1
    else:
        l+=1

print(arr)