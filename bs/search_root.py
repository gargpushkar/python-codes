class Solution:
	def searchRoot(self, n: int) -> int:
		# add your logic here
		l, h = 0, 10000
		ans = 0
		while(l<=h):
			mid = (l+h)//2
			if mid*mid == n:
				return mid
			if mid*mid < n:
				l = mid + 1
				ans = mid
			else:
				h = mid - 1
		return ans
		
sol = Solution()
num = 145678
print(sol.searchRoot(num))