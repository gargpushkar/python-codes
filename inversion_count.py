# A = [3, 4, 12, 32, 1, 44, 2, 21, 11, 0]
A = [1, 20, 6, 4, 5]
n = len(A)

def merge_sort(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid+1, right)
        inv_count += merge(arr, temp, left, mid, right)
    return inv_count

def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left
    j = mid+1
    k = left
    while(i <= mid and j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            inv_count += mid-i+1
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
    return inv_count

temp = [0]*n
print(merge_sort(A, temp, 0, n-1))
print(A)