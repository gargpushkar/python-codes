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
        version1 = version1.split('.')
        version2 = version2.split('.')

        ver1 = [int(num) for num in version1 if num]
        ver2 = [int(num) for num in version2 if num]
        n1 = len(ver1)
        n2 = len(ver2)
        
        for i in range(n1, n2):
            ver1.append(0)

        for i in range(n2, n1):
            ver2.append(0)

        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1
        return 0
