import time
start_time = time.perf_counter()
from collections import namedtuple

# Branch and bound algorithm for solving the Knapsack problem.
# Items are sorted by density (value / weight) from highest to lowest.
# Depth first search
# "relax_infinite" means the estimator function (which provides a best case scenario estimate for each
# node of the tree) assumes that infinite weight capacity remains so all future items can be taken.


# Set path to data file
file = "data/ks_30_0"

# No need to modify below here
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    result = Knapsack(input_data)
    result.sorter()
    result.branchBound(0)
    result.outputter()
    return result.output_data

class Knapsack:
    def __init__(self, input_data):
        lines = input_data.split('\n')

        firstLine = lines[0].split()
        self.item_count = int(firstLine[0])
        self.capacity = int(firstLine[1])

        self.items = []
        self.max_estimate = 0

        for i in range(1, self.item_count + 1):
            line = lines[i]
            parts = line.split()
            self.items.append(Item(i - 1, int(parts[0]), int(parts[1])))
            self.max_estimate += int(parts[0])

        self.best_value = 0
        self.solution = []
        self.value_taken = 0
        self.sorted_taken = [0]*self.item_count
        self.room = self.capacity
        self.alarm = 0

    def sorter(self):
        self.items_sorted = sorted(self.items, key=lambda item: item.value, reverse=True)

    def branchBound(self, start):

        if self.value_taken > self.best_value:
            self.best_value = self.value_taken
            self.solution = self.sorted_taken.copy()

        for i in range(start, self.item_count):
            if self.estimator(i) <= self.best_value:
                return

            value = self.items_sorted[i].value
            weight = self.items_sorted[i].weight

            if self.room >= weight:
                # Pack item
                self.value_taken += value
                self.room -= weight
                self.sorted_taken[i] = 1
                self.branchBound(i + 1)

                # Unpack item
                self.value_taken -= value
                self.room += weight
                self.sorted_taken[i] = 0

    def estimator(self, start):
        remaining_value = 0
        for i in range(start, self.item_count):
            remaining_value += self.items_sorted[i].value

        return self.value_taken + remaining_value

    def outputter(self):
        taken = [0] * self.item_count
        for i in range(len(self.items_sorted)):
            index = self.items_sorted[i].index
            taken[index] = self.solution[i]

        self.output_data = self.best_value, taken

with open(file, "r") as input_file:
    input_data = input_file.read()
    value, taken = solve_it(input_data)
    print("Number of items taken:", sum(taken))
    print(f"Value collected = {value}")
    print(f"Items taken = {taken}")

print("Time taken to find solution (seconds):", time.perf_counter() - start_time)
