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

def hill_climbing(distance_matrix):
    """Perform a single run of Hill Climbing for TSP."""
    num_cities = len(distance_matrix)
    
    # Start with a random solution
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, distance_matrix)
    
    while True:
        neighbors = generate_neighbors(current_route)
        best_neighbor = None
        best_distance = current_distance

        for neighbor in neighbors:
            neighbor_distance = calculate_total_distance(neighbor, distance_matrix)
            if neighbor_distance < best_distance:
                best_neighbor = neighbor
                best_distance = neighbor_distance

        if best_neighbor:
            current_route = best_neighbor
            current_distance = best_distance
        else:
            break
    
    return current_route, current_distance

def random_restart_hill_climbing(distance_matrix, restarts=10):
    """Perform Random-Restart Hill Climbing for TSP."""
    best_route = None
    best_distance = float("inf")
    
    for i in range(restarts):
        print(f"\n🔄 Restart {i + 1}/{restarts}...")
        route, distance = hill_climbing(distance_matrix)
        print(f"➡️ Route: {' -> '.join(map(str, route))} -> {route[0]} | Distance: {distance}")
        
        if distance < best_distance:
            best_route = route
            best_distance = distance

    return best_route, best_distance

# Taking dynamic input from the user
def main():
    num_cities = int(input("Enter the number of cities: "))
    print("\nEnter the distance matrix row by row (space-separated values):")
    distance_matrix = []

    for i in range(num_cities):
        row = list(map(int, input(f"Enter distances from city {i} to other cities: ").split()))
        distance_matrix.append(row)
    
    restarts = int(input("\nEnter the number of random restarts: "))
    
    best_route, best_distance = random_restart_hill_climbing(distance_matrix, restarts)
    
    print("\n✅ Best Route After Random-Restart Hill Climbing:", " -> ".join(map(str, best_route)), "->", best_route[0])
    print("✅ Best Distance:", best_distance)

if __name__ == "__main__":
    main()
