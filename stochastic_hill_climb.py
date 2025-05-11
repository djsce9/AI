import random

def calculate_total_distance(route, distance_matrix):
    """Calculate the total distance of the given route."""
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities):
        total_distance += distance_matrix[route[i]][route[(i + 1) % num_cities]]
    return total_distance

def generate_neighbors(current_route):
    """Generate all possible neighbors by swapping two cities."""
    neighbors = []
    num_cities = len(current_route)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            neighbor = current_route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def stochastic_hill_climbing(distance_matrix):
    """Perform Stochastic Hill Climbing for TSP."""
    num_cities = len(distance_matrix)
    
    # Step 1: Generate an initial random solution
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, distance_matrix)
    
    print("\nInitial Route:", " -> ".join(map(str, current_route)), "->", current_route[0])
    print("Initial Distance:", current_distance)
    
    iteration = 0
    
    # Stochastic Hill Climbing
    while True:
        neighbors = generate_neighbors(current_route)
        random.shuffle(neighbors)  # Randomize neighbors
        
        improved = False
        for neighbor in neighbors:
            neighbor_distance = calculate_total_distance(neighbor, distance_matrix)
            if neighbor_distance < current_distance:
                # Randomly choose a better neighbor
                current_route = neighbor
                current_distance = neighbor_distance
                iteration += 1
                print(f"\nIteration {iteration}:")
                print("New Better Route:", " -> ".join(map(str, current_route)), "->", current_route[0])
                print("New Better Distance:", current_distance)
                improved = True
                break
        
        if not improved:
            break
    
    return current_route, current_distance

# Taking dynamic input from the user
def main():
    num_cities = int(input("Enter the number of cities: "))
    print("\nEnter the distance matrix row by row (space-separated values):")
    distance_matrix = []

    for i in range(num_cities):
        row = list(map(int, input(f"Enter distances from city {i} to other cities: ").split()))
        distance_matrix.append(row)
    
    best_route, best_distance = stochastic_hill_climbing(distance_matrix)
    
    print("\n✅ Optimal Route:", " -> ".join(map(str, best_route)), "->", best_route[0])
    print("✅ Optimal Distance:", best_distance)

if __name__ == "__main__":
    main()
