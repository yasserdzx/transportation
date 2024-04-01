import numpy as np
from scipy.optimize import linprog

# Given cost matrix
cost = np.array([
    [21, 10, 15, 14],  
    [15, 13, 21, 11],  
    [26, 17, 20, 25]   
])

allocation_plan = np.array([
    [0, 300, 0, 0],
    [180, 120, 0, 150],
    [180, 0, 220, 0]
])


supply = np.array([300, 450, 400])
demand = np.array([360, 420, 220, 150])

num_suppliers, num_consumers = allocation_plan.shape
A_eq = np.zeros((num_suppliers + num_consumers, num_suppliers * num_consumers))

for i in range(num_suppliers):
    A_eq[i, i * num_consumers:(i + 1) * num_consumers] = 1

for j in range(num_consumers):
    A_eq[num_suppliers + j, j::num_consumers] = 1

b_eq = np.concatenate([supply, demand])


bounds = [(0, None) for _ in range(num_suppliers * num_consumers)]


result = linprog(c=cost.flatten(), A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

if result.success:
    
    optimal_allocation = result.x.reshape((num_suppliers, num_consumers))
    print("Optimal Allocation Plan:")
    print(optimal_allocation)
    print("Solution found.")
    print("Total cost:", result.fun)
else:
    print("No solution found.")
