"""
Use this Queue class(already implemented)


class Queue:
	def __init__(self, capacity=0):

	def isFull(self) -> bool:

	def isEmpty(self) -> bool:

	def size(self) -> int:

	def front(self) -> int:

	def back(self) -> int:
 
	def push(self, element: int) -> None:
 
	def pop(self) -> None:

"""
class Queue:
	pass

# Using 2 queues
class Stack:
	def __init__(self, capacity=0):
		self.queue1 = Queue(capacity)
		self.queue2 = Queue(capacity)

	def isEmpty(self) -> bool:
		return self.queue1.isEmpty()

	def size(self) -> int:
		return self.queue1.size()

	def top(self) -> int:
		return self.queue1.front()

	def push(self, element: int) -> None:
		self.queue2.push(element)
		while self.queue1.size():
			elem = self.queue1.front()
			self.queue2.push(elem)
			self.queue1.pop()
		self.queue1, self.queue2 = self.queue2, self.queue1

	def pop(self) -> None:
		self.queue1.pop()



# Using 1 queue
class Stack:
	def __init__(self, capacity=0):
		self.queue1 = Queue(capacity)

	def isEmpty(self) -> bool:
		return self.queue1.isEmpty()

	def size(self) -> int:
		return self.queue1.size()

	def top(self) -> int:
		return self.queue1.front()

	def push(self, element: int) -> None:
		self.queue1.push(element)
		n = self.queue1.size()
		for _ in range(1, n):
			elem = self.queue1.front()
			self.queue1.push(elem)
			self.queue1.pop()

	def pop(self) -> None:
		self.queue1.pop()

