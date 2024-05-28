# Travelling Salesman Problem using Genetic Algorithm

This project implements a Genetic Algorithm (GA) to solve the Traveling Salesman Problem (TSP). The TSP is an NP-hard problem in combinatorial optimization where the objective is to find the shortest possible route that visits a list of cities and returns to the origin city.

### Features
- Representation of cities (nodes) and distances between them (edges) using data classes.
- Generation of an initial population of possible solutions.
- Fitness evaluation of solutions based on total travel distance.
- Selection of parent solutions using tournament selection.
- Crossover of parent solutions to produce new offspring.
- Mutation of solutions to maintain genetic diversity.
- Iterative evolution of the population to find the optimal solution.

### Prerequisites
- Python >3.6
- NumPy

### Instalation
1. Clone the repository:
 ```bash
 git clone https://github.com/florin-romulescu/tsp-genetic-algorithm
 cd tsp-genetic-algorithm
 ```

 2. Build and run docker image :
 ```bash
    docker build -t tsp-genetic-algorithm .
    docker run --rm tsp-genetic-algorithm
 ```

 ### Usage:
 1. Construct a graph in the settings.json file by this model:
```json
{
    nodes : [
        {"id" : 1, "name" : "A", "x": 0, "y": 0},
        ...
    ],
    edges : [
        {"node1": 1, "node2": 2, "distance": 2},
        ...
    ]
}
```
2. Run main.py
```bash
python3 main.py
```
