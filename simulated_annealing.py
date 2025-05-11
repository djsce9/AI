import random
import math

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

def simulated_annealing(distance_matrix, initial_temp, cooling_rate, max_iterations):
    """Perform Simulated Annealing for TSP."""
    num_cities = len(distance_matrix)
    
    # Step 1: Generate an initial random solution
    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, distance_matrix)
    best_route = current_route[:]
    best_distance = current_distance
    
    print("\nInitial Route:", " -> ".join(map(str, current_route)), "->", current_route[0])
    print("Initial Distance:", current_distance)
    
    temperature = initial_temp
    iteration = 0
    
    while temperature > 0.1 and iteration < max_iterations:
        # Generate a random neighbor
        neighbor = generate_random_neighbor(current_route)
        neighbor_distance = calculate_total_distance(neighbor, distance_matrix)
        
        # Calculate the change in distance
        delta = neighbor_distance - current_distance
        
        # Accept the neighbor with probability depending on the temperature
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_route = neighbor
            current_distance = neighbor_distance
        
        # Update the best solution found
        if current_distance < best_distance:
            best_route = current_route[:]
            best_distance = current_distance
        
        # Cool down the temperature
        temperature *= cooling_rate
        iteration += 1
        
        print(f"Iteration {iteration}: Temp = {temperature:.4f} | Distance = {current_distance}")
    
    return best_route, best_distance

# Taking dynamic input from the user
def main():
    num_cities = int(input("Enter the number of cities: "))
    print("\nEnter the distance matrix row by row (space-separated values):")
    distance_matrix = []

    for i in range(num_cities):
        row = list(map(int, input(f"Enter distances from city {i} to other cities: ").split()))
        distance_matrix.append(row)
    
    initial_temp = float(input("\nEnter the initial temperature (e.g., 1000): "))
    cooling_rate = float(input("Enter the cooling rate (e.g., 0.99): "))
    max_iterations = int(input("Enter the maximum number of iterations: "))

    best_route, best_distance = simulated_annealing(distance_matrix, initial_temp, cooling_rate, max_iterations)
    
    print("\n✅ Optimal Route using Simulated Annealing:", " -> ".join(map(str, best_route)), "->", best_route[0])
    print("✅ Optimal Distance:", best_distance)

if __name__ == "__main__":
    main()
