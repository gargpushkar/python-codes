arr = [2, 3, 1, 5, 1]
i = 0
n = len(arr)

while(i<n):
    if arr[i] != arr[arr[i] -1]:
        arr[arr[i] -1], arr[i] = arr[i], arr[arr[i] -1]
    else:
        i+=1

for i in range(n):
    if arr[i] != i+1:
        missing_number = i+1
        duplicate_number = arr[i]

print(missing_number, duplicate_number)