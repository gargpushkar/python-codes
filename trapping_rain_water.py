arr = [3, 0, 0, 2, 0, 4]
arr = [ 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
n = len(arr)
max_left = [0]*n
max_left[0] = arr[0]
for i in range(1, n):
    max_left[i] = max(max_left[i-1], arr[i])

max_right = [0]*n
max_right[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    max_right[i] = max(max_right[i+1], arr[i])
# max_water_level = []
# for i in range(n):
#     max_water_level.append(min(max_left[i], max_right[i]))

total_water = 0
for i in range(n):
    total_water+= min(max_left[i], max_right[i]) - arr[i]

print(total_water)