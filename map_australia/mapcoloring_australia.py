def is_valid(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(assignment, graph, colors, nodes):
    if len(assignment) == len(nodes):
        return assignment
    unassigned = [n for n in nodes if n not in assignment][0]
    for color in colors:
        if is_valid(unassigned, color, assignment, graph):
            assignment[unassigned] = color
            result = backtracking(assignment, graph, colors, nodes)
            if result:
                return result
            del assignment[unassigned]
    return None

def solve_map(graph, colors):
    nodes = list(graph.keys())
    return backtracking({}, graph, colors, nodes)

australia_graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

solution = solve_map(australia_graph, colors)

print("Australia Map Coloring:")
for k, v in solution.items():
    print(k, ":", v)