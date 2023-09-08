class minHeap():
	def __init__(self):
		self.capacity = 20
		self.size = 0
		self.items = [None] * self.capacity

	def parent_index(self, index): return int((index - 1) / 2)
	def left_child_index(self, index): return (index * 2) + 1
	def right_child_index(self, index): return (index * 2) + 2

	def parent_exists(self, index): return self.parent_index(index) >= 0
	def left_child_exists(self, index): return self.left_child_index(index) < self.size
	def right_child_exists(self, index): return self.right_child_index(index) < self.size

	def parent(self, index): return self.items[self.parent_index(index)]
	def left_child(self, index): return self.items[self.left_child_index(index)]
	def right_child(self, index): return self.items[self.right_child_index(index)]

	def swap(self, i, j):
		temp = self.items[i]
		self.items[i] = self.items[j]
		self.items[j] = temp

	def ensure_capacity(self):
		if self.size < self.capacity: return
		self.capacity = self.capacity * 2
		new_items = [None] * self.capacity
		for i, item in enumerate(self.items):
			new_items[i] = item
		self.items = new_items

	def peak(self):
		return self.items[0]

	def poll(self):
		if self.size == 0: return ('No Element Exists')
					
		value = self.items[0]
		self.items[0] = self.items[self.size - 1]
		self.items[self.size - 1] = None
		self.size = self.size - 1
		self.heapify_down()

		return value

	def insert(self, value):
		self.ensure_capacity()

		self.items[self.size] = value
		self.size = self.size + 1
		self.heapify_up()
		
	def heapify_down(self):	
		curr = 0
		
		while self.left_child_exists(curr):
			min_child_index = self.left_child_index(curr)	
			if self.right_child_exists(curr) and self.right_child(curr) < self.left_child(curr):
				min_child_index = self.right_child_index(curr)

			if self.items[curr] > self.items[min_child_index]:
				self.swap(curr, min_child_index)

			curr = min_child_index

	def heapify_up(self):
		curr = self.size - 1

		while self.parent_exists(curr) and self.items[curr] < self.parent(curr):
			self.swap(curr, self.parent_index(curr))
			curr = self.parent_index(curr) 

heap = minHeap()
values = [12, 3, 45, 2, 8, 9, 22, 10, 15]
for val in values:
	heap.insert(val)
for i in range(8):
	print(heap.poll())

