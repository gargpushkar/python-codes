# Aggressive Cows
# You are given an array consisting of n integers which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. 
# You are given the task of assigning stalls to k cows such that the minimum distance between any two of them is the maximum possible.
# The first line of input contains two space-separated integers n and k.
# The second line contains n space-separated integers denoting the position of the stalls.

# Example 1:
# Input:
# n=5 
# k=3
# stalls = [1 2 4 8 9]
# Output:
# 3
# Explanation:
# The first cow can be placed at stalls[0], 
# the second cow can be placed at stalls[2] and 
# the third cow can be placed at stalls[3]. 
# The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.

# Example 2:
# Input:
# n=5 
# k=3
# stalls = [10 1 2 7 5]
# Output:
# 4
# Explanation:
# The first cow can be placed at stalls[0],
# the second cow can be placed at stalls[1] and
# the third cow can be placed at stalls[4].
# The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.



n=5
k= 3
stalls= [10, 1, 2, 7, 5]
# ans=5
class Solution:
    def solve(self,n,k,stalls):        
        def is_safe(stalls, n, k, mid):
            cows = 1
            last_pos = stalls[0]
            for i in stalls:
                if i-last_pos >= mid:
                    cows += 1
                    last_pos = i
                if cows >= k:
                    return True
            return False
        stalls.sort()
        left = 0
        right = max(stalls)
        ans = -1
        while left <= right:
            mid = left + (right-left)//2
            if is_safe(stalls, n, k, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


sol = Solution()
print(sol.solve(n, k, stalls))
