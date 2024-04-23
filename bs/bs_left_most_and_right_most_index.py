# Left most and right most index
# Given a sorted array with possibly duplicate elements. The task is to find indexes of first and last occurrences of an element X in the given array.

# Note: If the element is not present in the array return {-1,-1} as pair.

 

# Example 1:

# Input:
# N = 9
# v[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
# X = 5
# Output:
# 2 5
# Explanation:
# Index of first occurrence of 5 is 2
# and index of last occurrence of 5 is 5.
# Example 2:

# Input:
# N = 9
# v[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}
# X = 7
# Output:
# 6 6

#User function Template for python3

class Solution:
    def indexes(self, v, x):
        # Your code goes here
        n = len(v)
        l = 0
        r = n-1
        i = -1
        while l<=r:
            mid = l + (r-l)//2
            if v[mid] == x:
                i = mid
                l = mid + 1
            elif v[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        if i == -1:
            return [-1, -1]
        l = 0
        r = n-1
        j = -1
        while l<=r:
            mid = l + (r-l)//2
            if v[mid] == x:
                j = mid
                r = mid - 1
            elif v[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return [j, i]


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()
