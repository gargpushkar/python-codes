# Equal Sum Partition
# The partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is the same. 

# Examples: 

# Input: arr[] = {1, 5, 11, 5}
# Output: true 
# The array can be partitioned as {1, 5, 5} and {11}

# Input: arr[] = {1, 5, 3}
# Output: false 
# The array cannot be partitioned into equal sum sets.


# My approach
arr = [0, 4, 2, 2, 0, 1, 3, 0, 1]
n = len(arr)
total_sum = sum(arr)
half_sum = sum(arr)//2
ans=[False]
def equal_sum(arr, n, current_sum, total_sum, ans):
    if n == 0:
        return
    if current_sum == total_sum:
        ans[0] = True
        return 
    if arr[n-1] <= half_sum:
        equal_sum(arr, n-1, current_sum + arr[n-1], total_sum - arr[n-1], ans)
        equal_sum(arr, n-1, current_sum, total_sum, ans)
    else:
        equal_sum(arr, n-1, current_sum, total_sum, ans)

equal_sum(arr, n, 0, total_sum, ans)
print(ans)


# Better approach
arr = [0, 4, 2, 2, 0, 1, 3, 0, 1]
# arr = [1, 5, 11, 5]
n = len(arr)
total_sum = sum(arr)
half_sum = sum(arr)//2


def equal_sum(arr, n, s_sum):
    if n == 0:
        return False
    
    if s_sum == 0:
        return True
    
    if arr[n-1] <= s_sum:
        return equal_sum(arr, n-1, s_sum) or equal_sum(arr, n-1, s_sum-arr[n-1])
    else:
        return equal_sum(arr, n-1, s_sum)
    
print(False if total_sum%2!=0 else equal_sum(arr, n, half_sum))


# Memoization -- DP
arr = [0, 4, 2, 2, 0, 1, 3, 0, 1]
n = len(arr)
total_sum = sum(arr)
half_sum = sum(arr)//2
t = []
for i in range(n+1):
    t.append([-1]*(half_sum+1))

def memo_equal_sum(arr, n, half_sum, t):
    if half_sum == 0:
        return True
    if n == 0:
        return False
    
    if t[n][half_sum] != -1:
        return t[n][half_sum]
    
    if arr[n-1] > half_sum:
        t[n][half_sum] = memo_equal_sum(arr, n-1, half_sum, t)
        return t[n][half_sum]
    else:
        t[n][half_sum] = memo_equal_sum(arr, n-1, half_sum, t) or memo_equal_sum(arr, n-1, half_sum-arr[n-1], t)
        return t[n][half_sum]

print(False if total_sum%2!=0 else memo_equal_sum(arr, n, half_sum, t))


# Tabular DP
arr = [0, 4, 2, 2, 0, 1, 3, 0, 1]
n = len(arr)
total_sum = sum(arr)
half_sum = sum(arr)//2
t = []
for i in range(n+1):
    t.append([-1]*(half_sum+1))


def tab_equal_sum(arr, n, half_sum, t):
    for i in range(n+1):
        for j in range(half_sum+1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True

    t[0][0] = True

    for i in range(1, n+1):
        for j in range(1, half_sum+1):
            if arr[i-1] > half_sum:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
    return t[n][half_sum]

print(False if total_sum%2!=0 else tab_equal_sum(arr, n, half_sum, t))