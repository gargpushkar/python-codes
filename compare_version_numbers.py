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

version_1 = "2.3.000"
version_2 = "2.3"
i = 0 
j = 0
n = len(version_1)
m = len(version_2)
while i < n and j < m:
    if version_1[i] > version_2[j]:
        print(1)
    elif version_1[i] < version_2[j]:
        print(-1)
    i+=1
    j+=1
    
# version_1 = "".join(list(map(str, list(map(int, version_1.split("."))))))
# version_2 = "".join(list(map(str, list(map(int, version_2.split("."))))))

# if version_1 == version_2:
#     print(0)
# elif version_1 > version_2:
#     print(1)
# else:
#     print(-1)
