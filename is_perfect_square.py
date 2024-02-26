# https://workat.tech/problem-solving/practice/is-perfect-square
# Given a positive integer num, write a function that returns true if num is a perfect square else false.

# Note: Do not use the in-built methods to calculate square root or power.

class Solution:
	def isPerfectSquare(self, n: int) -> bool:
		# add your logic here
		# l, h = 0, n - 1
		l, h = 0, 10000
		while(l<=h):
			mid = (l+h)//2
			if mid * mid < n:
				l = mid + 1
			elif mid * mid > n:
				h = mid - 1
			else:
				return True
		return False


sol = Solution()
print(sol.isPerfectSquare(2))
print(sol.isPerfectSquare(4), True)
print(sol.isPerfectSquare(6))
print(sol.isPerfectSquare(8))
print(sol.isPerfectSquare(16), True)
print(sol.isPerfectSquare(32))
print(sol.isPerfectSquare(25), True)
print(sol.isPerfectSquare(100), True)
print(sol.isPerfectSquare(1))