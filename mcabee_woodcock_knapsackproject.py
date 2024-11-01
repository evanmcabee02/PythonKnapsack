import random

# GA parameters
population_size = 100
mutation_rate = 0.01
crossover_rate = 0.7
max_generations = 50

# Problem-specific parameters
#knapsack_capacity = 10  # Example capacity
#items = [(2, 5), (3, 5), (5, 1), (1, 5), (2, 1)]  # Example items (weight, value)

knapsack_capacity = 165  # Example capacity
items = [(23, 92), (31, 57), (29, 49), (44, 68), (53, 60), (38, 43), (63, 67), (85,84), (89, 87), (82, 72)]  # Example items (weight, value)

# Helper function to calculate the fitness of a chromosome
def fitness(chromosome, items, capacity):
    weight, value = 0, 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            weight += items[i][0]
            value += items[i][1]
            if weight > capacity:
                return 0, 0  # We return 0 for both value and weight if over capacity
    return value, weight  # Now returns a tuple of (value, weight)

# Selection function to select the fittest individuals
def select(population, fitnesses):
    # We will sort the population based on the value part of the fitness tuple
    sorted_population = [x for _, x in sorted(zip([f[0] for f in fitnesses], population), key=lambda pair: pair[0], reverse=True)]
    return sorted_population[:int(len(population) * crossover_rate)]

# Crossover function to create new offspring
def crossover(selected):
  offspring = []
  for _ in range(len(selected) // 2):
      parent1 = random.choice(selected)
      parent2 = random.choice(selected)
      child1, child2 = parent1[:], parent2[:]
      if random.random() < crossover_rate:
          crossover_point = random.randint(1, len(parent1) - 2)
          child1 = parent1[:crossover_point] + parent2[crossover_point:]
          child2 = parent2[:crossover_point] + parent1[crossover_point:]
      offspring.extend([child1, child2])
  return offspring

# Mutation function to introduce genetic diversity
def mutate(offspring):
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            mutation_point = random.randint(0, len(offspring[i]) - 1)
            offspring[i][mutation_point] = 1 - offspring[i][mutation_point]
    return offspring

# Initialize population
population = [[random.randint(0, 1) for _ in range(len(items))] for _ in range(population_size)]

# GA execution
for generation in range(max_generations):
    fitnesses = [fitness(chromosome, items, knapsack_capacity) for chromosome in population]
    selected = select(population, fitnesses)
    offspring = crossover(selected)
    offspring = mutate(offspring)
    population = selected + offspring[:len(population) - len(selected)]
    # Update the print to show both value and weight of the best chromosome
    best_value, best_weight = max(fitnesses)
#    print(f"Generation {generation}: Best Value: {best_value}, Best Weight: {best_weight}")

# Find the best solution at the end of the Genetic Algorithm
best_solution = max(population, key=lambda chromosome: fitness(chromosome, items, knapsack_capacity)[0])
best_value, best_weight = fitness(best_solution, items, knapsack_capacity)

# Print the final output in the desired format
print("Solution:", ' '.join(map(str, best_solution)))
print(f"Value: {best_value}     Weight: {best_weight}")
