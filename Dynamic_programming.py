import time
start_time = time.perf_counter()
import numpy as np
from collections import namedtuple

# Dynamic programming algorithm for solving the Knapsack problem.

# Set path to data file
file = "data/ks_30_0"

# No need to modify below here
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    #Created placeholder item so that item indexing would start at 1 to match the dynamic programming table.
    items = ["Placeholder item"]

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i, int(parts[0]), int(parts[1])))

    value, taken = dynamicProgramming(item_count, capacity, items)

    return value, taken

def dynamicProgramming(item_count, capacity, items):

    table = np.zeros((item_count + 1,capacity + 1), dtype=int)

    for i in range(1, item_count + 1):
        item_weight = items[i].weight
        item_value = items[i].value
        for room in range(capacity + 1):
            if room >= item_weight:
                take_value = table[i-1][room-item_weight] + item_value
                leave_value = table[i-1][room]
                table[i][room] = max(take_value, leave_value)
            else:
                table[i][room] = table[i-1][room]
    optimum_value = table[-1][-1]
    taken = traceBack(table, item_count, capacity, items)

    return optimum_value, taken

def traceBack(table, item_count, capacity, items):
    taken = [0]*(item_count + 1)
    taken[0] = "Placeholder item, remember to delete"
    room = capacity
    for item_index in range(item_count, 0, -1):
        if item_index != items[item_index].index:
            print("Error: index doesn't match")
            exit()
        if table[item_index][room] != table[item_index - 1][room]:
            room -= items[item_index].weight
            taken[item_index] = 1

    # Delete placeholder item.
    del taken[0]
    return taken

with open(file, "r") as input_file:
    input_data = input_file.read()
    value, taken = solve_it(input_data)
    print("Number of items taken:", sum(taken))
    print(f"Value collected = {value}")
    print(f"Items taken = {taken}")

print("Time taken to find solution (seconds):", time.perf_counter() - start_time)
