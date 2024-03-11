# Compare Version Numbers
# Given two version numbers, compare them.

# A version number consists of one or more revisions connected by a dot.
# Each revisions consists of digits and may contain leading zeroes. Each revision consists atleast one digit.

# Revisions are 0-indexed from left to right.
# To compare two versions, compare revisions in the left-to-right order. Revisions are compared using their integer value ignoring any leading zeroes.

# Example 1
# version 1: 1.1.0
# version 2: 1.2.0

# version 2 > version 1.

# Example 2
# version 1: 1.001.2
# version 2: 1.1.2

# version 2 = version 1.

# Example 3
# version 1: 1.100.2
# version 2: 1.1.2

# version 2 < version 1.

# Example 4
# version 1: 1.2.1.1
# version 2: 1.2

# version 2 < version 1.

class Solution:
	def compareVersion(self, version1: str, version2: str) -> int:
		# add your logic here
		# version_1 = list(map(int, version1.split(".")))
		version1 = version1.split(".")
		version_1 = []
		for i in version1:
			if i:
				version_1.append(int(i))
		# version_2 = list(map(int, version2.split(".")))
		version2 = version2.split(".")
		version_2 = []
		for i in version2:
			if i:
				version_2.append(int(i))
		n1 = len(version_1)
		n2 = len(version_2)
		if n1>n2:
			for i in range(n2, n1):
				version_2.append(0)
		else:
			for i in range(n1, n2):
				version_1.append(0)
		for i in range(len(version_1)):
			if version_1[i] > version_2[i]:
				return 1
			elif version_1[i] < version_2[i]:
				return -1
		return 0

