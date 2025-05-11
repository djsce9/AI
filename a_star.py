import heapq

def a_star_search(start, goal, graph, heuristics):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, []))
    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current in closed_set:
            continue

        path = path + [current]
        if current == goal:
            return path, g

        closed_set.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristics.get(neighbor, float("inf"))
                heapq.heappush(open_list, (new_f, new_g, neighbor, path))

    return None, float("inf") 

def get_graph_input():
    graph = {}
    n = int(input("Enter the total number of nodes in the graph: "))
    
    for _ in range(n):
        node = input("\nEnter node name: ").strip()
        graph[node] = []
        edges = int(input(f"Enter the number of edges from {node}: "))
        
        for _ in range(edges):
            while True:
                neighbor = input("Enter connected node: ").strip()
                try:
                    cost = int(input(f"Enter cost to {neighbor}: "))
                    graph[node].append((neighbor, cost))
                    break
                except ValueError:
                    print("Error: Please enter a valid cost (integer).")

    return graph

def get_heuristics_input(nodes):
    heuristics = {}
    print("\nEnter heuristic values for each node:")
    for node in nodes:
        while True:
            try:
                heuristics[node] = int(input(f"Heuristic value for {node}: "))
                break
            except ValueError:
                print("Error: Please enter a valid heuristic value (integer).")
    
    return heuristics

if __name__ == "__main__":
    print("A* Search Algorithm\n")
    
    # Input graph
    graph = get_graph_input()
    
    # Get all nodes in the graph
    nodes = list(graph.keys())
    
    # Input heuristics for each node
    heuristics = get_heuristics_input(nodes)
    
    # Input start and goal nodes with validation
    while True:
        start = input("\nEnter the start node: ").strip()
        if start in nodes:
            break
        else:
            print("Error: Start node not found in the graph.")

    while True:
        goal = input("Enter the goal node: ").strip()
        if goal in nodes:
            break
        else:
            print("Error: Goal node not found in the graph.")
    
    # Perform A* Search
    path, cost = a_star_search(start, goal, graph, heuristics)
    
    # Display results
    print("\nA* Search Result:")
    if path:
        print("Optimal Path using A*:", " -> ".join(path))
        print("Total Cost:", cost)
    else:
        print("No path found!")
