# Knapsack

Solves the one-dimensional Knapsack problem

## Description

As described by Wikipedia (https://en.wikipedia.org/wiki/Knapsack_problem):  
"The knapsack problem is a problem in combinatorial optimization: Given a set 
of items, each with a weight and a value, determine the number of each item 
to include in a collection so that the total weight is less than or equal 
to a given limit and the total value is as large as possible."

There are several algorithms to solve this problem, two of which are:
* dynamic programming (https://en.wikipedia.org/wiki/Dynamic_programming)
* branch and bound tree search (https://en.wikipedia.org/wiki/Branch_and_bound)

This project implements both of these algorithms independently.
Both algorithms are guaranteed to find the optimal solution, however the
branch and bound algorithm finds the solution much faster than the
dynamic programming algorithm.

## Authors

Ethan Watkins

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details

## Acknowledgements

Coursera Discrete Optimization course by Professor Pascal Van Hentenryck 
and Dr. Carleton Coffrin, University of Melbourne  
https://www.coursera.org/learn/discrete-optimization