# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/

import math
class Solution:
    def minimumPushes(self, word: str) -> int:
        hash_map = {}
        for i in word:
            hash_map[i] = hash_map.get(i, 0) + 1
        arr = sorted(hash_map.values(), reverse=True)
        total = 0
        for i in range(1, len(arr)+1):
            total += math.ceil(i/8)*arr[i-1]
        return total
