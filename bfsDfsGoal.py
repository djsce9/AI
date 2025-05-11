from collections import deque, defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    
    if start == goal:
        print(f"Start is the goal: {start}")
        return

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    print(f"BFS Path: {' -> '.join(map(str, new_path))}")
                    return
            visited.add(node)
    print("BFS: No path found")

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    visited.add(start)

    if start == goal:
        print(f"DFS Path: {' -> '.join(map(str, path))}")
        return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = path + [neighbor]
            if dfs(graph, neighbor, goal, visited, new_path):
                return True
    return False

# Dynamic Input with Error Handling
graph = defaultdict(list)
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    while True:
        try:
            u, v = input("Enter edge (u v): ").split()
            add_edge(graph, u, v)
            break
        except ValueError:
            print("Error: Please enter exactly two nodes (u v).")

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

print("\nBreadth-First Search:")
bfs(graph, start, goal)

print("\nDepth-First Search:")
if not dfs(graph, start, goal):
    print("DFS: No path found")
