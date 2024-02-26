n = 10
arr = [0, 1]

for i in range(2, n+1):
    arr.append(arr[i-1] + arr[i-2])

print(arr)

arr2 = []
def fib_rec(n, arr2):
    if n == 0:
        return arr2
    if n == 1:
        return arr2
    fib_rec(n-1, arr2)
    arr2.append(arr2[n-1] + arr2[n-2])
    return arr2


arr2 = [0, 1]
print(fib_rec(n, arr2))
