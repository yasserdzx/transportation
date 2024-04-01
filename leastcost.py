import numpy as np

def least_cost_method(cost_matrix, supply, demand):
    cost_matrix, supply, demand = np.array(cost_matrix), np.array(supply), np.array(demand)
    result = np.zeros_like(cost_matrix)
    mask = np.ones_like(cost_matrix, dtype=bool)
    
    while np.any(supply > 0) and np.any(demand > 0):
        masked_costs = np.where(mask, cost_matrix, np.inf)
        i, j = np.unravel_index(np.argmin(masked_costs), cost_matrix.shape)
        shipment = min(supply[i], demand[j])
        result[i, j] = shipment
        supply[i] -= shipment
        demand[j] -= shipment
        if supply[i] == 0:
            mask[i, :] = False
        if demand[j] == 0:
            mask[:, j] = False
            
    total_cost = (result * cost_matrix).sum()
    return result, total_cost

cost_matrix = [[21, 10, 15, 14], [15, 13, 21, 11], [26, 17, 20, 25]]
supply = [300, 450, 400]
demand = [360, 420, 220, 150]

result, total_cost = least_cost_method(cost_matrix, supply, demand)
print("Allocation Plan:")
print(result)
print("Total Cost:", total_cost)
