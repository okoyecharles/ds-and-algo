# Topological Sort

graph = {
	'a': ['b', 'c'],
	'b': ['c'],
	'c': []
}
# expected return: "cba"

courses = {
	'1': ['2'],
	'2': ['3', '4'],
	'4': ['6', '7'],
	'3': ['5', '6'],
	'5': [], '6': [], '7': [],
	'8': ['7']	
}
# expected return 56374218
# NB: There is no unique order, as long as every course dependency comes before the course, The output is valid


def topsort(graph):
	res = []
	traversed = set()

	def dfs(node, visited):
		if node in visited: return False
		if node in traversed or node not in graph: return

		visited.add(node)
		traversed.add(node)		
		
		# post order traversal
		for child in graph[node]:
			nocycle = dfs(child, visited)
			if nocycle == False: return False
		res.append(node)
		visited.remove(node)

	for node in graph:
		if node in traversed: continue
		if dfs(node, set()) == False: return ""

	return "".join(res)

print(topsort(graph))
print(topsort(courses))
