from itertools import product
from random import randint

# Number of locations
num_locations = 5

# Define types of game elements
elements = ["bridge", "river", "puzzle", "hazard", "artifact", "clue", "treasure", "rainy_weather", "marsh"]

# Initialize game elements for each location
locations = []
for i in range(num_locations):
    location = {elem: f"{i}_{elem}" for elem in elements}
    locations.append(location)

# Function to create constraints
def generate_constraints():
    constraints = []

    # Core game constraints
    for loc in locations:
        # Example constraints
        constraints.append((loc["river"], loc["bridge"], loc["clue"]))  # River -> (Bridge & Clue)
        constraints.append((loc["hazard"], loc["artifact"], loc["treasure"]))  # Hazard -> (not Artifact or not Treasure)
        constraints.append((loc["rainy_weather"], loc["marsh"]))  # Rainy Weather -> Marsh

    return constraints

# Function to check if a solution satisfies all constraints
def satisfies_constraints(solution, constraints):
    for constraint in constraints:
        if not evaluate_constraint(solution, *constraint):
            return False
    return True

# Function to evaluate a single constraint
def evaluate_constraint(solution, *args):
    # Simple implication logic: A -> (B & C)
    if len(args) == 3:
        A, B, C = args
        return not solution[A] or (solution[B] and solution[C])
    elif len(args) == 2:
        A, B = args
        return not solution[A] or solution[B]
    return True

# Function to print the current game setup
def print_game_setup(setup):
    print("\nCurrent Game Setup:")
    for i, loc in enumerate(locations):
        active_elements = [elem for elem in elements if setup[loc[elem]]]
        print(f"  Location {i + 1}: {', '.join(active_elements) if active_elements else 'No elements'}")
    print()

# Function to provide hints for missing victory conditions
def check_victory_conditions(solution):
    hints = []
    if not any(solution[loc["treasure"]] for loc in locations):
        hints.append("Ensure at least one location contains a treasure.")
    return hints

# Function to randomize the setup of locations
def randomize_locations():
    setup = {}
    for loc in locations:
        for elem in elements:
            setup[loc[elem]] = randint(0, 1) == 1
    return setup

# Function to test all combinations for the first location
def test_all_combos():
    constraints = generate_constraints()
    for elem in elements:
        solution = {var: False for loc in locations for var in loc.values()}
        solution[locations[0][elem]] = True
        print(f"\nTesting with {elem} set to True at Location 1:")
        print_game_setup(solution)
        if satisfies_constraints(solution, constraints):
            display_solution(solution)
        else:
            print(f"Constraint violation with {elem} set to True.")

# Function to find a solution
def solve_game():
    constraints = generate_constraints()

    # Generate all possible solutions
    all_variables = [var for loc in locations for var in loc.values()]
    all_combinations = product([False, True], repeat=len(all_variables))

    for combo in all_combinations:
        solution = dict(zip(all_variables, combo))
        if satisfies_constraints(solution, constraints):
            return solution
    return None

# Function to display the solution
def display_solution(sol):
    if not sol:
        print("No solution found. Victory condition not met.")
        hints = check_victory_conditions(sol)
        if hints:
            print("Hints:")
            for hint in hints:
                print(f"  - {hint}")
        return

    # Check if victory conditions are satisfied
    victory = any(sol[loc["treasure"]] for loc in locations)
    if victory:
        print("Victory achieved! Treasure was found.")
        for i, loc in enumerate(locations):
            found_elements = [elem.split("_")[1] for elem in sol if sol[elem] and elem.startswith(f"{i}_")]
            print(f"Location {i + 1}: {' '.join(found_elements)}")
    else:
        print("No victory. Treasure or key elements missing.")
        hints = check_victory_conditions(sol)
        if hints:
            print("Hints:")
            for hint in hints:
                print(f"  - {hint}")

# Main function
if __name__ == "__main__":
    choice = input('Enter 0 to choose the locations setup, 1 to test all combinations, or any other key to randomize: ')

    if choice == '0':
        game_setup = randomize_locations()
        print_game_setup(game_setup)
    elif choice == '1':
        test_all_combos()
    else:
        game_setup = randomize_locations()
        print_game_setup(game_setup)

    # Find and display the optimal strategy
    solution = solve_game()
    display_solution(solution)