# Largest number in K swaps
# Given a number K and string str of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of str at most K times.

# Example 1:
# Input:
# K = 4
# str = "1234567"
# Output:
# 7654321
# Explanation:
# Three swaps can make the
# input 1234567 to 7654321, swapping 1
# with 7, 2 with 6 and finally 3 with 5

# Example 2:
# Input:
# K = 3
# str = "3435335"
# Output:
# 5543333
# Explanation:
# Three swaps can make the input
# 3435335 to 5543333, swapping 3 
# with 5, 4 with 5 and finally 3 with 4 

s = "3435335"
k = 3


def solve(s, k, starting_index, ans):
    if k == 0 or starting_index == len(s)-1:
        return
    max_elem = -1
    for i in range(starting_index+1, len(s)):
        max_elem = max(max_elem, int(s[i]))
    for i in range(starting_index+1, len(s)):
        if s[starting_index] < s[i] and int(s[i]) == max_elem:
            s[starting_index], s[i] = s[i], s[starting_index]
            t1 = int("".join(s))
            t2 = int("".join(ans[0]))
            if t1 > t2:
                ans[0] = s[::]
            
            solve(s, k-1, starting_index+1, ans)
            s[starting_index], s[i] = s[i], s[starting_index]
    
    solve(s, k, starting_index+1, ans)

ans = [list(s)]
solve(list(s), k, 0, ans)
print("".join(ans[0]))
