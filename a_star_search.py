import heapq


graph = {
    'Chennai': {
        'Kanchipuram': 2,
        'Vellore': 5
    },
    'Kanchipuram': {
        'Chennai': 2,
        'Krishnagiri': 6
    },
    'Vellore': {
        'Chennai': 5,
        'Krishnagiri': 4
    },
    'Krishnagiri': {
        'Kanchipuram': 6,
        'Vellore': 4,
        'Bangalore': 3
    },
    'Bangalore': {
        'Krishnagiri': 3
    }
}


h = {
    'Chennai': 10,
    'Kanchipuram': 8,
    'Vellore': 7,
    'Krishnagiri': 3,
    'Bangalore': 0
}

def a_star_search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = {}

    print(f"Starting A* Search from '{start}' to '{goal}':\n")
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current in visited and visited[current] <= g:
            continue
        visited[current] = g
        print(f"Visiting {current}: g={g}, h={h[current]}, f={f}")

        if current == goal:
            return path, g

        for neighbor, cost in graph[current].items():
            new_g = g + cost
            new_f = new_g + h[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

if __name__ == "__main__":
    path, cost = a_star_search(graph, h, 'Chennai', 'Bangalore')
    print("\nOptimal Route:", " -> ".join(path))
    print("Total Route Cost:", cost, "km")
