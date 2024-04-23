# Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
A = [3, 4, 12, 32, 1, 44, 2, 21, 11]

for i in range(len(A)):
    min_elem = A[i]
    min_elem_index = i
    for j in range(i, len(A)):
        if min_elem > A[j]:
            min_elem = A[j]
            min_elem_index = j
    A[min_elem_index], A[i] = A[i], A[min_elem_index]

print(A)
