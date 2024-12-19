from collections import defaultdict


# Edges connect a node to it's neigbor with a weight
class Edge:
    def __init__(self, n, w):
        self.neighbor = n
        self.weight = w


# Nodes should have:
# - A heuristic (h)
# - The cost from the start node (g)
class Node:
    def __init__(self, v, h):
        self.value = v
        self.h = h
        self.g = float("inf")

        # Track path taken to arrive at goal
        self.previous = None


# Weighted Graph is represented by an adjacency list (adj)
class WeightedGraph:
    def __init__(self):
        self.adj = defaultdict(set)


# Create nodes with respective heuristics
s = Node("S", 5)
a = Node("A", 3)
b = Node("B", 4)
c = Node("C", 2)
d = Node("D", 6)
g = Node("G", 0)

# Create graph and add its edges
graph = WeightedGraph()

graph.adj[s].add(Edge(a, 1))
graph.adj[s].add(Edge(g, 10))
graph.adj[a].add(Edge(b, 2))
graph.adj[a].add(Edge(c, 1))
graph.adj[b].add(Edge(d, 5))
graph.adj[c].add(Edge(d, 3))
graph.adj[c].add(Edge(g, 4))
graph.adj[d].add(Edge(g, 2))


def a_star_search(graph: WeightedGraph, start: Node, goal: Node):
    start.g = 0
    open = {start}
    closed = set()
    iteration = 0

    # Search as long as there is a node in the open set
    while len(open) > 0:
        iteration += 1
        print_search_info(iteration, open, closed)

        # Get node with minimum fitness value in open set
        curr_node = get_minimum_fitness_node(open)

        # Remove the node from the open set
        open.remove(curr_node)
        print("- Picked " + curr_node.value + " from Open Set")
        print()

        # Return the node if it the goal node
        if curr_node == goal:
            print(get_search_path(curr_node), end=" ")
            print("[Path found]")
            return curr_node

        # Loop through each edge of the node
        for edge in graph.adj[curr_node]:
            neighbor = edge.neighbor
            weight = edge.weight

            curr_node_fitness_number = curr_node.g + curr_node.h
            neighbor_fitness_number = neighbor.g + neighbor.h

            # Skip if neighbor has been visited
            if neighbor in closed:
                continue

            # Only add a neighbor to the open set if either:
            # - neighbor is not in the open set OR
            # - the neighbor's new g (cost from the start node) is less than the current g
            if neighbor not in open or curr_node.g + edge.weight < neighbor.g:
                neighbor.g = curr_node.g + edge.weight
                neighbor.previous = curr_node
                if neighbor not in open:
                    open.add(neighbor)

        # Add node to the closed set when all it's neighbors have been evaluated
        closed.add(curr_node)

    print("No path found")
    return None


def get_minimum_fitness_node(set):
    # search the open set for the node with the minimum fitness number
    # i.e. the minimum value of g + h
    minimum_fitness_number = float("inf")
    minimum_fitness_node = None

    for node in set:
        if minimum_fitness_node == None:
            minimum_fitness_node = node
            minimum_fitness_number = node.g + node.h
        else:
            node_fitness_number = node.g + node.h
            if node_fitness_number < minimum_fitness_number:
                minimum_fitness_node = node
                minimum_fitness_number = node_fitness_number

    return minimum_fitness_node


def get_search_path(goal: Node):
    # print the path taken from start to goal node
    path = goal.value
    curr = goal.previous
    while curr:
        path = curr.value + " -> " + path
        curr = curr.previous
    return path


def print_search_info(iteration: int, open: {Node}, closed: set):
    print("Iteration", iteration, end=":\n")
    open_set_items = ""
    for item in open:
        open_set_items += ", " + item.value
    closed_set_items = ""
    for item in closed:
        closed_set_items += ", " + item.value
    print("Open Set: " + "(" + open_set_items[2:] + ")")
    print("Closed Set: " + "(" + closed_set_items[2:] + ")")
    print()

start = s
goal = g
a_star_search(graph, start, goal)
