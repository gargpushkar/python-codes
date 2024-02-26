# Largest Subarray of sum K

# Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.

# For Input:
# 1
# 7 5
# 4 1 1 1 2 3 5
# your output is: 
# 4 . 

arr = [1,2,3,7,5]
n = 5
k = 12
# arr = [4, 1, 1, 1, 2, 3, 5]
# n = 7
# k = 5
# TODO
ans = 0
i=0
j=0
arr_sum = 0
while(i<n and j<n):
    arr_sum += arr[j]
    if arr_sum == k:
        ans = max(ans, j-i+1)
        arr_sum -= arr[i]
        i+=1
        j+=1
    elif arr_sum > k:
        arr_sum -= arr[i]
        i+=1
    else:
        j+=1

print(ans)