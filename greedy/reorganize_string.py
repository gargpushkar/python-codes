# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Example 1:
# Input: s = "aab"
# Output: "aba"

# Example 2:
# Input: s = "aaab"
# Output: ""

from collections import Counter
import heapq

s = "bbbaaabb"

hash_map = dict(Counter(s))
max_heap = []
heapq.heapify(max_heap)
for key in hash_map:
    heapq.heappush(max_heap, [-hash_map[key], key])

ans = ""
while max_heap:
    elem1 = heapq.heappop(max_heap)
    if max_heap:
        elem2 = heapq.heappop(max_heap)
        ans += elem1[1] + elem2[1]
        elem1[0] += 1
        elem2[0] += 1
        if elem1[0] != 0:
            heapq.heappush(max_heap, elem1)
        if elem2[0] != 0:
            heapq.heappush(max_heap, elem2)
    elif -elem1[0] > 1:
        ans = ""
        break
    else:
        ans += elem1[1]
print(ans)