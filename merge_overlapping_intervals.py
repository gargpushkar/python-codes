# https://workat.tech/problem-solving/practice/merge-overlap-intervals
# Given a list of intervals, merge them to get a list of non-overlapping intervals.

# intervali = [starti, endi]

# Example:
# Intervals: [[1, 2], [2, 3], [1, 4], [5, 6]]

# [1, 2] and [2, 3] can be merged to form [1, 3].
# Now, [1, 3] and [1, 4] can be merged to form [1, 4].
# [1, 4] and [5, 6] have no intersection.
# Hence above intervals are merged to form:
# [[1, 4], [5, 6]]

# Note that the final list should be in ascending order.
from typing import List

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # hash_map = {}
        # for i in intervals:
        #     if i[0] not in hash_map:
        #         hash_map[i[0]] = i[1]
        #     else:
        #         hash_map[i[0]] = max(hash_map[i[0]], i[1])
        # updated_intervals = []
        # for i in hash_map:
        #     updated_intervals.append((i, hash_map[i]))

        a,b = intervals[0][0], intervals[0][1]
        ans = []
        for itr, i in enumerate(intervals):
            if itr == 0:
                continue
            c,d = i[0], i[1]
            if c <= b:
                b = max(d, b)
            else:
                ans.append([a, b])
                a,b = c,d 
        ans.append([a, b])
        return ans

