class Stack:
	def __init__(self):
		self.stack = []
	
	def push(self, element):
		self.stack.append(element)
	
	def pop(self):
		return self.stack.pop()
	
	def size(self):
		return len(self.stack)


class Solution:
	def isBalancedParentheses(self, s: str) -> bool:
		# add your logic here
		stack = Stack()
		for i in s:
			if i in ['(', '{', '[']:
				stack.push(i)
			else:
				if stack.size():
					elem = stack.pop()
					if i == ')' and elem != '(':
						return 0
					elif i == ']' and elem != '[':
						return 0
					elif i == '}' and elem != '{':
						return 0	
				else:
					return 0
		if len(self.stack.size()):
			return 0
		return 1



sol = Solution()
print(sol.isBalancedParentheses("[{[][][]{}{}[]()()}"))