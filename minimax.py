import math

# Minimax function with decision tracking
def minimax(depth, node_index, is_max, scores, height, path):
    # Base case: If we reach a terminal node
    if depth == height:
        return scores[node_index], path + [str(scores[node_index])]

    # If it's the maximizing player's turn
    if is_max:
        # Explore the left child (L) and right child (R)
        left_value, left_path = minimax(depth + 1, node_index * 2, False, scores, height, path + ["L"])
        right_value, right_path = minimax(depth + 1, node_index * 2 + 1, False, scores, height, path + ["R"])

        # Choose the maximum value from the two children
        if left_value > right_value:
            return left_value, left_path
        else:
            return right_value, right_path
    else:
        # Explore the left child (L) and right child (R)
        left_value, left_path = minimax(depth + 1, node_index * 2, True, scores, height, path + ["L"])
        right_value, right_path = minimax(depth + 1, node_index * 2 + 1, True, scores, height, path + ["R"])

        # Choose the minimum value from the two children
        if left_value < right_value:
            return left_value, left_path
        else:
            return right_value, right_path

# Take dynamic input from the user
while True:
    try:
        scores = list(map(int, input("Enter terminal node values (space-separated, power of 2): ").split()))
        if (math.log2(len(scores))).is_integer():  # Check if the length is a power of 2
            break
        else:
            print("Error: The number of values must be a power of 2 (e.g., 2, 4, 8, 16, etc.). Try again!")
    except ValueError:
        print("Invalid input! Please enter integer values.")

# Compute the height of the tree
tree_height = int(math.log2(len(scores)))

# Start Minimax Algorithm
optimal_value, optimal_path = minimax(0, 0, True, scores, tree_height, [])

# Print results
print(f"\nThe optimal value is: {optimal_value}")
print(f"The optimal decision path is: {' -> '.join(optimal_path)}")
