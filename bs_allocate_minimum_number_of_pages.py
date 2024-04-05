# Allocate minimum number of pages
# https://www.youtube.com/watch?v=2JSQIhPcHQg&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=21
# You have N books, each with A[i] number of pages. M students need to be allocated contiguous books, with each student getting at least one book.
# Out of all the permutations, the goal is to find the permutation where the sum of maximum number of pages in a book allotted to a student should be minimum, out of all possible permutations.

# Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

# Example 1:
# Input:
# N = 4
# A[] = {12,34,67,90}
# M = 2
# Output:113
# Explanation:Allocation can be done in 
# following ways:
# {12} and {34, 67, 90} Maximum Pages = 191
# {12, 34} and {67, 90} Maximum Pages = 157
# {12, 34, 67} and {90} Maximum Pages = 113.
# Therefore, the minimum of these cases is 113, which is selected as the output.

# Example 2:
# Input:
# N = 3
# A[] = {15,17,20}
# M = 2
# Output:32
# Explanation: Allocation is done as {15,17} and {20}

# Related Problems For Practice :
# Book Allocation Problem (GFG)
# Aggressive cow (spoj)
# Prata and roti (spoj)
# EKO (spoj)
# Google kickstart A Q-3 2020
# Painter Partition Problem
# Below Leetcode Problems
# 1482 Minimum Number of Days to Make m Bouquets
# 1283 Find the Smallest Divisor Given a Threshold
# 1231 Divide Chocolate
# 1011 Capacity To Ship Packages In N Days
# 875 Koko Eating Bananas
# Minimize 
# 774 Max Distance to Gas Station
# 410 Split Array Largest Sum

class Solution:
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if N < M:
            return -1
        
        def is_valid(A, N, M, mid):
            no_students = 1
            total = 0
            for i in A:
                total += i
                if total > mid:
                    no_students += 1
                    total = i
                if no_students > M:
                    return False
            return True
        
        left = max(A)
        right = sum(A)
        ans = -1
        while left<=right:
            mid  = left + (right-left)//2
            if is_valid(A, N, M, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
# A = [15, 17, 20]
A = [13, 31, 37, 45, 46, 54, 55, 63, 73, 84, 85]
N = len(A)
M = 9
sol = Solution()
print(sol.findPages(A, N, M))