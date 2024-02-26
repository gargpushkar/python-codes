# Dutch National Flag
# Sort an array A where each of the elements belong to the set: {0, 1, 2}.

# Expected Time Complexity: O(n)

# Try to solve it without storing the count of 0s, 1s and 2s.
A = [2, 2, 0, 1]
# A = [1, 0, 1, 2, 2]
# A = [1, 0, 0, 0]
n = len(A)
l=0
r=n-1
mid=0

while(mid<=r):
    if A[mid] == 0:
        A[mid], A[l] = A[l], A[mid]
        l+=1
        mid+=1
    elif A[mid] == 2:
        A[r], A[mid] = A[mid], A[r]
        r-=1
    else:
        mid+=1

print(A)