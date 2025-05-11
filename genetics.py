import random

# Step 1: Initialize Population
def initialize_population(pop_size, chrom_length):
    return [[random.randint(0, 1) for _ in range(chrom_length)] for _ in range(pop_size)]

# Step 2: Fitness Function (Example: Maximize sum of genes)
def fitness(chromosome):
    return sum(chromosome)  # The goal is to maximize the number of 1s

# Step 3: Selection (Roulette Wheel Selection)
def selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitness_scores):
        current += f
        if current > pick:
            return population[i]
    return population[-1]

# Step 4: Crossover (Single Point and Two-Point)
def crossover(parent1, parent2, method='single'):
    if method == 'single':
        point = random.randint(1, len(parent1) - 1)
        return (parent1[:point] + parent2[point:], parent2[:point] + parent1[point:])
    elif method == 'two':
        point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))
        return (
            parent1[:point1] + parent2[point1:point2] + parent1[point2:],
            parent2[:point1] + parent1[point1:point2] + parent2[point2:]
        )
    else:
        raise ValueError("Invalid crossover method. Use 'single' or 'two'.")

# Step 5: Mutation (Flip Bits)
def mutation(chromosome, mutation_rate):
    return [
        gene if random.random() > mutation_rate else 1 - gene 
        for gene in chromosome
    ]

# Step 6: Genetic Algorithm Main Function
def genetic_algorithm(pop_size, chrom_length, mutation_rate, generations, crossover_method):
    population = initialize_population(pop_size, chrom_length)
    
    for gen in range(generations):
        # Calculate fitness for each individual
        fitness_scores = [fitness(ind) for ind in population]
        new_population = []

        # Generate new population using selection, crossover, and mutation
        for _ in range(pop_size // 2):
            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2, crossover_method)
            new_population.extend([mutation(child1, mutation_rate), 
                                   mutation(child2, mutation_rate)])

        # Update the population
        population = new_population

        # Track best individual in the generation
        best_individual = max(population, key=fitness)
        print(f'Generation {gen + 1}: Best Fitness = {fitness(best_individual)}, Solution = {best_individual}')

    # Return the best solution found
    return max(population, key=fitness)

# User Inputs with Error Handling
def user_inputs():
    while True:
        try:
            pop_size = int(input("Enter Population Size (Positive Integer): "))
            if pop_size > 0:
                break
            else:
                print("Error: Population size must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    while True:
        try:
            chrom_length = int(input("Enter Chromosome Length (Positive Integer): "))
            if chrom_length > 0:
                break
            else:
                print("Error: Chromosome length must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    while True:
        try:
            mutation_rate = float(input("Enter Mutation Rate (0-1): "))
            if 0 <= mutation_rate <= 1:
                break
            else:
                print("Error: Mutation rate must be between 0 and 1.")
        except ValueError:
            print("Error: Please enter a valid decimal number.")

    while True:
        try:
            generations = int(input("Enter Number of Generations (Positive Integer): "))
            if generations > 0:
                break
            else:
                print("Error: Number of generations must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    while True:
        crossover_method = input("Enter Crossover Method (single/two): ").strip().lower()
        if crossover_method in ['single', 'two']:
            break
        else:
            print("Error: Please choose 'single' or 'two' for crossover method.")
    
    return pop_size, chrom_length, mutation_rate, generations, crossover_method

# Run Genetic Algorithm
print("Genetic Algorithm\n")
pop_size, chrom_length, mutation_rate, generations, crossover_method = user_inputs()
best_solution = genetic_algorithm(pop_size, chrom_length, mutation_rate, generations, crossover_method)
print("\nBest Solution Found:", best_solution)
print("Best Fitness:", fitness(best_solution))
