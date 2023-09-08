"""
example-facts:
m = 3.28 ft
ft = 12 in
hr = 60 min
min = 60 sec
example queries:
2 m = ? in -> answer 78.72
13 in = ? m -> answer 0.330 (roughly)
13 in = ? hr -> "not convertible!"
"""

conversion_facts = {
'm' : ('3.28', 'ft'),
'ft' : ('12', 'in'),
'hr' : ('60', 'min'),
'min' : ('60', 'sec'),
}

# Analysis: n = number of units/nodes, m = number of edges
def process_facts (facts):
    graph = {} # Space O(n + m)
    visited = set() # Space O(n)

    for unit_1 in facts: # Time O(n + m) 
        unit_2 = facts[unit_1][1]

        if not unit_1 in visited:
            graph[unit_1] = []
            visited.add(unit_1)
        if not unit_2 in visited:
            graph[unit_2] = []
            visited.add(unit_2)

        graph[unit_1].append((float(facts[unit_1][0]), unit_2))
        graph[unit_2].append((1.0 / float(facts[unit_1][0]), unit_1))


    return graph

def convertUnit (val, facts, convert_from, convert_to):
    val = float(val)
    facts = process_facts(facts) # Space  O(n + m)

    def dfs (curr_val, curr_unit, end_unit, path): # Time O(n + m)
        if curr_unit in path: # path >> Space O(n)
            return None
        if curr_unit == end_unit:
            return curr_val

        path.add(curr_unit)
        for rate, next_unit in facts[curr_unit]:
            conversion = dfs(curr_val * rate, next_unit, end_unit, path)
            if conversion is not None:
                return conversion
                break
        path.remove(curr_unit)

        return None

    return dfs(val, convert_from, convert_to, set())

queries = [
    (2, conversion_facts, 'm', 'in'),
    (13, conversion_facts, 'in', 'm'),
    (13, conversion_facts, 'in', 'hr'),
    (1, conversion_facts, 'hr', 'sec'),
]

for q in queries:
    print(convertUnit(q[0], q[1], q[2], q[3]))
