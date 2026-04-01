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

telangana_graph = {
    "Adilabad": ["Komaram Bheem", "Nirmal"],
    "Komaram Bheem": ["Adilabad", "Mancherial"],
    "Mancherial": ["Komaram Bheem", "Peddapalli"],
    "Nirmal": ["Adilabad", "Nizamabad"],
    "Nizamabad": ["Nirmal", "Kamareddy"],
    "Kamareddy": ["Nizamabad", "Medak"],
    "Medak": ["Kamareddy", "Sangareddy", "Siddipet"],
    "Sangareddy": ["Medak", "Vikarabad"],
    "Vikarabad": ["Sangareddy", "Rangareddy"],
    "Rangareddy": ["Vikarabad", "Hyderabad"],
    "Hyderabad": ["Rangareddy", "Medchal"],
    "Medchal": ["Hyderabad", "Siddipet"],
    "Siddipet": ["Medak", "Medchal", "Jangaon"],
    "Jangaon": ["Siddipet", "Warangal"],
    "Warangal": ["Jangaon", "Hanamkonda"],
    "Hanamkonda": ["Warangal", "Mahabubabad"],
    "Mahabubabad": ["Hanamkonda", "Khammam"],
    "Khammam": ["Mahabubabad", "Bhadradri"],
    "Bhadradri": ["Khammam"],
    "Peddapalli": ["Mancherial", "Karimnagar"],
    "Karimnagar": ["Peddapalli", "Jagitial"],
    "Jagitial": ["Karimnagar", "Rajanna"],
    "Rajanna": ["Jagitial"],
    "Nalgonda": ["Suryapet", "Yadadri"],
    "Suryapet": ["Nalgonda", "Khammam"],
    "Yadadri": ["Nalgonda", "Hyderabad"],
    "Mahabubnagar": ["Narayanpet", "Wanaparthy"],
    "Narayanpet": ["Mahabubnagar"],
    "Wanaparthy": ["Mahabubnagar", "Nagarkurnool"],
    "Nagarkurnool": ["Wanaparthy", "Jogulamba"],
    "Jogulamba": ["Nagarkurnool"],
    "Mulugu": ["Warangal"],
    "Jayashankar": ["Mulugu"]
}

colors = ['Red', 'Green', 'Blue']

solution = solve_map(telangana_graph, colors)

print("Telangana Map Coloring:")
for k, v in solution.items():
    print(k, ":", v)