# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
A = [3, 4, 12, 32, 1, 44, 2, 21, 11]
len_A = len(A)

for i in range(len_A):
    j = i-1
    key = A[j+1]
    while j>=0 and key < A[j]:
        A[j+1] = A[j]
        j-=1
    A[j+1] = key

print(A)