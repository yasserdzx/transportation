import numpy as np

def north_west_corner(supply, demand, cost_matrix):
    i, j = 0, 0
    solution = np.zeros_like(cost_matrix)
    while i < len(supply) and j < len(demand):
        allocation = min(supply[i], demand[j])
        solution[i, j] = allocation
        supply[i] -= allocation
        demand[j] -= allocation
        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1
    total_cost = np.sum(solution * cost_matrix)
    return solution, total_cost

supply = np.array([300, 450, 400])
demand = np.array([360, 420, 220, 150])
cost_matrix = np.array([[21, 10, 15, 14], [15, 13, 21, 11], [26, 17, 20, 25]])

solution, total_cost = north_west_corner(supply, demand, cost_matrix)
print("Initial Transportation Plan:")
print(solution)
print(f"Total Cost: {total_cost}")
