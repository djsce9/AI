import random

def calculate_total_distance(route, distance_matrix):
    """Calculate the total distance of the given route."""
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities):
        total_distance += distance_matrix[route[i]][route[(i + 1) % num_cities]]
    return total_distance

def generate_random_neighbor(current_route):
    """Generate a random neighbor by swapping two cities."""
    neighbor = current_route[:]
    i, j = random.sample(range(len(current_route)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def first_choice_hill_climbing(distance_matrix, max_attempts=1000):
    """Perform First-Choice Hill Climbing for TSP."""
    num_cities = len(distance_matrix)
    
    # Step 1: Generate an initial random solution
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, distance_matrix)
    
    print("\nInitial Route:", " -> ".join(map(str, current_route)), "->", current_route[0])
    print("Initial Distance:", current_distance)
    
    attempts = 0
    
    # First-Choice Hill Climbing
    while attempts < max_attempts:
        neighbor = generate_random_neighbor(current_route)
        neighbor_distance = calculate_total_distance(neighbor, distance_matrix)
        
        if neighbor_distance < current_distance:
            current_route = neighbor
            current_distance = neighbor_distance
            attempts = 0  # Reset attempts because we improved
            print(f"\nNew Better Route: {' -> '.join(map(str, current_route))} -> {current_route[0]}")
            print("New Better Distance:", current_distance)
        else:
            attempts += 1
    
    return current_route, current_distance

# Taking dynamic input from the user
def main():
    num_cities = int(input("Enter the number of cities: "))
    print("\nEnter the distance matrix row by row (space-separated values):")
    distance_matrix = []

    for i in range(num_cities):
        row = list(map(int, input(f"Enter distances from city {i} to other cities: ").split()))
        distance_matrix.append(row)
    
    best_route, best_distance = first_choice_hill_climbing(distance_matrix)
    
    print("\n✅ Optimal Route:", " -> ".join(map(str, best_route)), "->", best_route[0])
    print("✅ Optimal Distance:", best_distance)

if __name__ == "__main__":
    main()
