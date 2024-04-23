# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
A = [3, 4, 12, 32, 1, 44, 2, 21, 11]
len_A = len(A)
for i in range(len_A):
    l_elem = A[i]
    for j in range(len_A- i - 1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

print(A)