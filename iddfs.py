def get_tree_input():
    tree = {}
    print("Enter tree in the format: parent child1 child2 ... (Type 'done' when finished)")
    while True:
        line = input("Enter node and its children: ").strip()
        if line.lower() == 'done':
            break
        parts = line.split()
        if parts:
            parent = parts[0]
            children = parts[1:]
            if parent in tree:
                tree[parent].extend(children)
            else:
                tree[parent] = children
    return tree

def depth_limited_search(tree, current_node, limit, depth, visited, path):
    if depth > limit:
        return
    visited.add(current_node)
    path.append(current_node)
    for neighbor in tree.get(current_node, []):
        if neighbor not in visited:
            depth_limited_search(tree, neighbor, limit, depth + 1, visited, path)

def iterative_deepening_search(tree, root, goal):
    depth = 0
    levels = {}
    total_nodes = set(tree.keys()).union(*tree.values())
    visited_total = set()
    goal_paths = []

    while len(visited_total) < len(total_nodes):
        visited = set()
        path = []
        depth_limited_search(tree, root, depth, 0, visited, path)
        if path:
            levels[depth] = path.copy()
            visited_total.update(visited)
            if goal in path:
                goal_paths.append((depth, path[:path.index(goal) + 1]))
        depth += 1

    print("\nTREE TRAVERSING")
    print(f"TOTAL LEVELS OF TREE = {depth - 1}")
    for lvl in range(depth):
        if lvl in levels:
            print(f"LEVEL {lvl}: {' '.join(levels[lvl])}")

    # Displaying best path to goal
    if goal_paths:
        best_path = min(goal_paths, key=lambda x: x[0])[1]
        print("\nBEST PATH TO REACH GOAL:")
        print(" -> ".join(best_path))
    else:
        print("\nGoal node is not reachable from the source.")

if __name__ == "__main__":
    # Input tree
    tree = get_tree_input()
    
    # Input source node with validation
    while True:
        source = input("\nEnter source node: ").strip()
        if source in tree:
            break
        else:
            print("Error: Source node not found in the tree. Please enter a valid source node.")

    # Input goal node
    goal = input("\nEnter goal node: ").strip()
    
    # Perform IDDFS traversal on the full tree
    iterative_deepening_search(tree, source, goal)
    print("\nIDDFS traversal completed.")
