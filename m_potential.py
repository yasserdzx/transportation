grid = [
[21, 10, 15, 14],
[15, 13, 21, 11],
[26, 17, 20, 25]
] # table
supply = [300, 450, 400] # supply
demand = [360, 420, 220, 150] # demand
INF = 10 ** 3
n = len(grid)
m = len(grid[0])
ans = 0
# hepler function for finding the row difference and the column difference
def findDiff(grid):
    rowDiff = []
    colDiff = []
    for i in range(len(grid)):
        arr = grid[i][:]
        arr.sort()
        rowDiff.append(arr[1] - arr[0])
    col = 0
    while col < len(grid[0]):
        arr = []
        for i in range(len(grid)):
            arr.append(grid[i][col])
        arr.sort()
        col += 1
        colDiff.append(arr[1] - arr[0])
    return rowDiff, colDiff
# loop runs until both the demand and the supply is exhausted
while max(supply) != 0 or max(demand) != 0:
    # finding the row and col difference
    row, col = findDiff(grid)
    # finding the maxiumum element in row difference array
    maxi1 = max(row)
    # finding the maxiumum element in col difference array
    maxi2 = max(col)
    # if the row diff max element is greater than or equal to col diff max element
    if maxi1 >= maxi2:
        for ind, val in enumerate(row):
            if val == maxi1:
            # finding the minimum element in grid index where the maximum was found in the row difference
                mini1 = min(grid[ind])
                for ind2, val2 in enumerate(grid[ind]):
                    if (val2 == mini1):
                        # calculating the min of supply and demand in that row and col
                        mini2 = min(supply[ind], demand[ind2])
                        ans += mini2 * mini1
                        # subtracting the min from the supply and demand
                        supply[ind] -= mini2
                        demand[ind2] -= mini2
                    # if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                        if (demand[ind2] == 0):
                            for r in range(n):
                                grid[r][ind2] = INF
                                # if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                        else:
                            grid[ind] = [INF for i in range(m)]
                        break
                break
                # if the row diff max element is greater than col diff max element
    else:
        for ind, val in enumerate(col):
            if val == maxi2:
            # finding the minimum element in grid index where the maximum was found in the col difference
                mini1 = INF
                for j in range(n):
                    mini1 = min(mini1, grid[j][ind])
                for ind2 in range(n):
                    val2 = grid[ind2][ind]
                    if val2 == mini1:
                        # calculating the min of supply and demand in that row and col
                        mini2 = min(supply[ind2], demand[ind])
                        ans += mini2 * mini1
                        # subtracting the min from the supply and demand
                        supply[ind2] -= mini2
                        demand[ind] -= mini2
                        # if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                        if (demand[ind] == 0):
                            for r in range(n):
                                grid[r][ind] = INF
                                # if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                        else:
                            grid[ind2] = [INF for i in range(m)]
                        break
                break
print("The basic feasible solution is ", ans)