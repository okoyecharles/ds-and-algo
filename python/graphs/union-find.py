# Union find
# uses: num of connected components, existence of cycle in graph

nodes = 9
edges = [[0, 1], [1, 2], [3, 4],  [4, 5], [5, 7]]

# 0 - 1 - 2
# 3 - 4 - 5 - 7
# 6
# 8

# Expected Output: [-3, 0, 0, -4, 3, 3, -1, 3, -1]
# negative nums represent: node is a head, num of nodes
# positive nums represent: pointer to the head

def unionfind(n, edges):
	def find(node):
		while par[node] >= 0: node = par[node]
		return node
	def union(n1, n2):
		par1, par2 = find(n1), find(n2)
		
		# cycle exists
		if par1 == par2: return -1
		
		if par[par1] <= par[par2]:
			par[par1] = par[par1] + par[par2]
			par[n2] = par1
		else:
			par[par2] = par[par2] + par[par1]
			par[n1] = par2

	par = [-1] * n
	for n1, n2 in edges:
		union(n1, n2)

	return par

print(unionfind(nodes, edges))
