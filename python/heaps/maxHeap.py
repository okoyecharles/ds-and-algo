class MaxHeap():
	def __init__ (self):
		self.heap = [None]
		self.capacity = len(self.heap)
		self.size = 0

	def get_parent_index (self, index): return int((index - 1) / 2)
	def get_left_child_index (self, index): return (index * 2) + 1 
	def get_right_child_index (self, index): return (index * 2) + 2

	def get_parent (self, index): return self.heap[self.get_parent_index(index)] 
	def get_left_child (self, index): return self.heap[self.get_left_child_index(index)] 
	def get_right_child (self, index): return self.heap[self.get_right_child_index(index)] 

	def parent_exists (self, index): return self.get_parent_index(index) >= 0
	def left_child_exists (self, index): return self.get_left_child_index(index) < self.size
	def right_child_exists (self, index): return self.get_right_child_index(index) < self.size

	def ensure_capacity (self):
		if self.size < self.capacity: return
		new_heap = [None] * (self.capacity * 2)
		for i, num in enumerate(self.heap):
			new_heap[i] = num
		self.heap = new_heap
		self.capacity = self.capacity * 2

	def swap (self, i, j):
		temp = self.heap[i]
		self.heap[i] = self.heap[j]
		self.heap[j] = temp

	def peek (self):
		return self.heap[0]

	def poll (self):
		if self.size < 1: raise Exception('Sorry the heap is empty')
		value = self.heap[0]
		self.heap[0] = self.heap[self.size - 1]
		self.heap[self.size - 1] = None
		self.size = self.size - 1

		self.heapify_down()

		return value

	def insert (self, value):
		self.ensure_capacity()
		self.heap[self.size] = value
		self.size = self.size + 1

		self.heapify_up()

	def heapify_up (self):
		curr = self.size - 1

		while self.parent_exists(curr) and self.get_parent(curr) < self.heap[curr]:
			self.swap(curr, self.get_parent_index(curr))
			curr = self.get_parent_index(curr)

	def heapify_down (self):
		curr = 0

		while self.left_child_exists(curr):
			max_child_index = self.get_left_child_index(curr)
			if self.right_child_exists(curr) and self.get_right_child(curr) > self.get_left_child(curr):
				max_child_index = self.get_right_child_index(curr)
			
			if self.heap[curr] > self.heap[max_child_index]:
				break
			self.swap(curr, max_child_index)
			curr = max_child_index

heap = MaxHeap()		
values = [3, 5, 61, 75, 2, 8, 16, 3, 9, 87]
for val in values:
	heap.insert(val)
print(heap.heap)
for i in range(len(values)):
	print(heap.poll())

