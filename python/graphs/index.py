class Graph:
	def __init__(self, nodes = []):
		self.graph = { n: [] for n in nodes }

	def add_edge(self, edge):
		n1, n2 = edge
		if n1 not in self.graph: self.graph[n1] = []
		if n2 not in self.graph: self.graph[n2] = []

		self.graph[n1].append(n2)
	
	def add_edges(self, edges):
		for edge in edges:
			self.add_edge(edge)

	def reversed(self):
		reverse_graph = {}
		
		for n1 in self.graph:
			for n2 in self.graph[n1]:
				if n1 not in reverse_graph: reverse_graph[n1] = []
				if n2 not in reverse_graph: reverse_graph[n2] = []

				reverse_graph[n2].append(n1)

		return reverse_graph
			
