import sys

class IDAStar:
    def __init__(self, graph, cost):
        self.graph = graph      # Adjacency list
        self.cost = cost        # Cost of each node
        self.goal = None
        self.path = []

    def search(self, node, g, threshold, path):
        """Performs depth-first search with cost constraint."""
        f = g + self.cost.get(node, float('inf'))  # f(n) = g(n) + cost(node)
        if f > threshold:
            return f  # Return new possible threshold
        if node == self.goal:
            self.path = path[:]  # Store the found path
            return "FOUND"

        min_threshold = float('inf')  # Smallest exceeded cost
        for neighbor in self.graph.get(node, []):  # Expand children
            if neighbor not in path:  # Avoid cycles
                path.append(neighbor)
                temp = self.search(neighbor, g + self.cost.get(neighbor, float('inf')), threshold, path)
                if temp == "FOUND":
                    return "FOUND"
                if temp < min_threshold:
                    min_threshold = temp
                path.pop()  # Backtrack
        return min_threshold  # Return updated threshold

    def ida_star(self, start, goal):
        """Main function to run IDA* iteratively."""
        self.goal = goal
        threshold = self.cost.get(start, float('inf'))  # Initial threshold = cost of start node

        while True:
            path = [start]
            temp = self.search(start, 0, threshold, path)
            if temp == "FOUND":
                print("\nOptimal Path using IDA*:", " → ".join(map(str, self.path)))
                print("Total Cost:", sum(self.cost[node] for node in self.path))
                return self.path
            if temp == float('inf'):
                print("\nNo path found!")
                return None  # No solution exists
            threshold = temp  # Increase threshold


# Taking dynamic input with error handling
def take_input():
    graph = {}
    cost = {}
    
    n = int(input("Enter number of nodes: "))
    print("\nEnter edges in the format: parent child (Type 'done' to stop)")

    while True:
        edge = input("Enter edge: ").strip()
        if edge.lower() == 'done':
            break
        try:
            u, v = edge.split()
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
        except ValueError:
            print("Error: Please enter two nodes (parent child).")
    
    print("\nEnter cost for each node:")
    for _ in range(n):
        while True:
            try:
                node, c = input("Node Cost: ").split()
                cost[node] = int(c)
                break
            except ValueError:
                print("Error: Please enter the node and cost correctly (node cost).")
    
    # Input start and goal nodes with validation
    while True:
        start = input("\nEnter start node: ").strip()
        if start in cost:
            break
        else:
            print("Error: Start node not found in the cost list.")

    while True:
        goal = input("Enter goal node: ").strip()
        if goal in cost:
            break
        else:
            print("Error: Goal node not found in the cost list.")
    
    return graph, cost, start, goal


# Run the algorithm
print("Iterative Deepening A* (IDA*) Search Algorithm\n")
graph, cost, start, goal = take_input()
ida = IDAStar(graph, cost)
ida.ida_star(start, goal)
