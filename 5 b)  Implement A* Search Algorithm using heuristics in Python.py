from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    # The tuple is (f_score, current_node, path, g_score)
    # The image initializes the f_score to 0
    frontier.put((0, start, [start], 0))
    
    visited = set()

    while not frontier.empty():
        f, current, path, g = frontier.get()

        if current == goal:
            print(f"Path found: {'->'.join(path)} with cost: {g}")
            return path

        if current in visited:
            continue
        
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                g_new = g + cost
                h_new = heuristic[neighbor]
                f_new = g_new + h_new
                frontier.put((f_new, neighbor, path + [neighbor], g_new))

    print("No path found")
    return None

# simple
# graph and heuristic
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 9},
    'E': {'G': 1},
    'F': {'G': 5},
    'G': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 6,
    'G': 0
}

# Run it
a_star_search(graph, 'A', 'G', heuristic)
