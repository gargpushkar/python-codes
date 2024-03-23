# Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
from typing import List

intervals = [[1,3],[6,9]]
newInterval = [2, 5]

# [[1, 3], [2, 5], [6, 9]]
# [[1,5],[6,9]]
intervals.append(newInterval)
ans = []

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        intervals.sort()
        previous_start = intervals[0][0]
        previous_end = intervals[0][1]
        for i in range(1, n):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            if current_start <= previous_end:
                previous_end = max(previous_end, current_end)
            else:
                ans.append([previous_start, previous_end])
                previous_start = current_start
                previous_end = current_end
                count += 1
        ans.append([previous_start, previous_end])
        print(ans)