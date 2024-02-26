# Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.


# A = [3, 4, 12, 32, 1, 44, 2, 21, 11, 0]


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]
#         merge_sort(L)
#         merge_sort(R)

#         # Below code is nothing but code to merge 2 sorted arrays
#         i, j, k = 0, 0, 0
#         while(i < len(L) and j < len(R)):
#             if L[i] > R[j]:
#                 arr[k] = R[j]
#                 k+=1
#                 j+=1
#             elif L[i] <= R[j]:
#                 arr[k] = L[i]
#                 k+=1
#                 i+=1
#         while(i < len(L)):
#             arr[k] = L[i]
#             i+=1
#             k+=1
        
#         while(j < len(R)):
#             arr[k] = R[j]
#             j+=1
#             k+=1
        
# merge_sort(A)
# print(A)



A = [3, 4, 12, 32, 1, 44, 2, 21, 11, 0]
n = len(A)

def merge_sort(arr, temp, left, right):
    if left < right:
        mid = (left + right)//2
        merge_sort(arr, temp, left, mid)
        merge_sort(arr, temp, mid+1, right)
        merge(arr, temp, left, mid, right)

def merge(arr, temp, left, mid, right):
    i = left
    j = mid+1
    k = left
    while(i <= mid and j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j+=1
        k+=1
    while(i <= mid):
        temp[k] = arr[i]
        i+=1
        k+=1
    while(j <= right):
        temp[k] = arr[j]
        j+=1
        k+=1
    
    for _ in range(left, right+1):
        arr[_] = temp[_]
    print(temp)

temp = [0]*n
merge_sort(A, temp, 0, n-1)
print(A)