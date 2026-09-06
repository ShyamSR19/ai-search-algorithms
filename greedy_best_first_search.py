import heapq


graph = {
    'Aarav': ['Bhavna', 'Chitra'],
    'Bhavna': ['Aarav', 'Divya', 'Esha'],
    'Chitra': ['Aarav', 'Farhan'],
    'Divya': ['Bhavna', 'Gita'],
    'Esha': ['Bhavna', 'Gita'],
    'Farhan': ['Chitra', 'Gita'],
    'Gita': ['Divya', 'Esha', 'Farhan', 'Hari'],
    'Hari': ['Gita']
}


h = {
    'Aarav': 4,
    'Bhavna': 3,
    'Chitra': 3,
    'Divya': 2,
    'Esha': 2,
    'Farhan': 2,
    'Gita': 1,
    'Hari': 0
}

def greedy_best_first_search(graph, h, start, goal):
    pq = [(h[start], start)]
    visited = set()
    parent = {start: None}

    print(f"Starting Greedy Best-First Search from '{start}' to '{goal}':\n")
    while pq:
        h_value, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        print(f"Visiting {current}, h={h_value}")

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(pq, (h[neighbor], neighbor))

    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()

    print("\nPath Found:", " -> ".join(path))
    print("Total Hops:", len(path) - 1)

if __name__ == "__main__":
    greedy_best_first_search(graph, h, 'Aarav', 'Hari')
