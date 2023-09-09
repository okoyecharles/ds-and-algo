# Strongly connected components
from index import Graph

edges = [
	('a', 'b'), ('b', 'c'), ('c', 'a'), ('b', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'd'), ('g', 'f'), ('g', 'h'), ('h', 'i'), ('i', 'j'), ('j', 'g'), ('j', 'k')
]

# Graph visualization
# a --- c     e        h --- i
#  \   /    /   \      |     |
#    b --- d --- f --- g --- j --- k
# 4 connected components
# expected return: [ [a, c, b], [e, d, f], [h, i, g, j], [k] ]

def scc(Graph):
	# populate the stack (post order)
	visited, stack = set(), []
	graph = Graph.graph

	def visit(node):
		if node in visited: return
		visited.add(node)
		for n in graph[node]:
			visit(n)
		stack.append(node)

	for node in graph:
		visit(node)

	visited, res = set(), []
	reversed = Graph.reversed() # reverse the graph
	
	# on each traversal create a component and append path
	def rvisit(node, component):
		if node in visited: return
		visited.add(node)
		component.append(node)
		for n in reversed[node]:
			rvisit(n, component)

	while len(stack) > 0:
		node = stack.pop()
		if node not in visited:
			res.append([])
			rvisit(node, res[-1])
	
	return res

graph = Graph()
graph.add_edges(edges)
print(scc(graph))
