# https://workat.tech/problem-solving/practice/kth-largest-from-data-stream

# Kth Largest Element From Data Stream
# Given an incoming stream of data, you need to find the kth largest element at each step.

# Implement the KthLargest class:

# KthLargest(int k) initializes the KthLargest object with the integer k and is called at the beginning.
# int add(int num) adds the integer num from the data stream, and returns the kth largest element until now.
# int add(int num) returns -1 if there aren't k elements so far.

import heapq


class KthLargest:
	def __init__(self, k: int):
		"""initialize your data structure here."""
		self.k = k
		self.min_heap = []
		heapq.heapify(self.min_heap)

	def add(self, num: int) -> int:
		heapq.heappush(self.min_heap, num)
        
		if len(self.min_heap) < self.k:
			return -1
		if len(self.min_heap) > self.k:
			heapq.heappop(self.min_heap)
		return self.min_heap[0]
		



"""
Your KthLargest object will be instantiated and called as such:

obj = KthLargest(k)
value = obj.add(num)

"""

obj = KthLargest(3)
print(obj.add(2))
print(obj.add(4))
print(obj.add(3))
print(obj.add(1))
print(obj.add(7))
print(obj.add(4))
print(obj.add(5))
print(obj.add(8))

