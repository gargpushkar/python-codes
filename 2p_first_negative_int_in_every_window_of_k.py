# First negative integer in every window of size k
# Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

arr = [12, -1, -7, 8, -15, 30, 16, 28]
n = 8
k = 3
arr = [-8, 2, 3, -6, 10]
n = 5
k = 2

# Brute Force
ans = []
for i in range(n-k+1):
    flag = False
    for j in range(i, i+k):
        if arr[j] < 0:
            flag = True
            ans.append(arr[j])
            break
    if not flag:
        ans.append(0)
    
print(ans)

# sliding window approach 
i=0
j=0
negative_array = []
ans2 = []
while(j<n):
    if arr[j] < 0:
        negative_array.append(arr[j])
    if j - i + 1 <k:
        j+=1
    elif j - i + 1 == k:
        if negative_array:
            ans2.append(negative_array[0])
        else:
            ans2.append(0)
        if negative_array and arr[i] == negative_array[0]:
            negative_array.pop(0)
        i+=1
        j+=1

print(ans2)