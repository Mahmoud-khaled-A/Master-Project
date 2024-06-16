```markdown
# Quoridor Strategy Master Project

## Overview
This repository contains the code and documentation for the project titled **"Mathematical Modelling and Implementation of Game Strategy for the Board Game Quoridor"**. The project explores various algorithms to develop strategies for mastering the board game Quoridor. The algorithms implemented include Minimax with Alpha-Beta Pruning (ABP), Expectimax (EM), and Monte Carlo Tree Search (MCTS), with the addition of probabilistic decision-making using the Softmax function.

## Contents
- **Source Code**: Implementation of the Quoridor game and the algorithms.
- **Documentation**: Detailed explanation of the project, methodologies, and findings.
- **Results**: Data and analysis from the experiments comparing different algorithms.

## Algorithms
### Minimax with Alpha-Beta Pruning (ABP)
The Minimax algorithm is a decision-making tool for two-player zero-sum games. Alpha-Beta Pruning optimizes the Minimax algorithm by pruning unnecessary branches, making it more efficient.

### Expectimax (EM)
The Expectimax algorithm extends Minimax to handle probabilistic scenarios. It calculates expected values for each decision, considering the probability distribution of possible opponent moves.

### Monte Carlo Tree Search (MCTS)
MCTS is a heuristic search algorithm combining precision tree searching with exploratory random sampling. It balances exploration and exploitation to find optimal moves.

### Softmax Function
The Softmax function introduces randomness in decision-making, preventing repetitive patterns and exploring a wider range of game states.



The `ABP-vs-MCTS` folder contains the following files:
- `ABP-vs-MCTS.csv`: This file contains the data of 100 games between the ABP and MCTS algorithms.
- `cluster1.csv`, `cluster2.csv`, `cluster3.csv`: These files contain the data of the original `ABP-Vs-MCTS.csv` file, which has been clustered into 3 separate files.
- `1.png`, `2.png`, `3.png`: These files show the end states for a game from each of the 3 clusters.
- `Execution Time vs. Number of Turns 1. png`: This is a scatter plot for the execution time vs. the number of turns in the games.
- `Execution Time vs. Number of Turns 2. png`: This is a scatter plot for the execution time vs. the number of turns in the games for the clustering groups.
- `algorithm_performance_comparison.png`: This image shows the number of wins for the algorithms in every cluster.

The `ABP_vs_EM` folder contains the following files:
- `ABP_vs_EM.csv`: This file contains the data of 100 games between the ABP and EM algorithms.
- `cluster1.csv`, `cluster2.csv`, `cluster3.csv`: These files contain the data of the original `ABP_vs_EM.csv` file, which has been clustered into 3 separate files.
- `1.png`, `2.png`, `3.png`: These files show the end states for a game from each of the 3 clusters.
- `Execution Time vs. Number of Turns 1. png`: This is a scatter plot for the execution time vs. the number of turns in the games.
- `Execution Time vs. Number of Turns 2. png`: This is a scatter plot for the execution time vs. the number of turns in the games for the clustering groups.
- `algorithm_performance_comparison.png`: This image shows the number of wins for the algorithms in every cluster.


The `EM_VS_ABP` folder contains the following files:
- `EM_VS_ABP.csv`: This file contains the data of 100 games between the EM and ABP algorithms.
- `cluster1.csv`, `cluster2.csv`, `cluster3.csv`: These files contain the data of the original `EM_VS_ABP.csv` file, which has been clustered into 3 separate files.
- `1.png`, `2.png`, `3.png`: These files show the end states for a game from each of the 3 clusters.
- `Execution Time vs. Number of Turns 1. png`: This is a scatter plot for the execution time vs. the number of turns in the games.
- `Execution Time vs. Number of Turns 2. png`: This is a scatter plot for the execution time vs. the number of turns in the games for the clustering groups.
- `algorithm_performance_comparison.png`: This image shows the number of wins for the algorithms in every cluster.



## Results
The project evaluates the performance of the algorithms based on win rates, execution times, and strategic depth in various game scenarios. The findings indicate that ABP is the most efficient but still lacks against human players. Detailed results and analysis can be found in the `docs/project_report.pdf` file.




## Contributors
- **Mahmoud Khaled Abdelkader** (mahmoudkh@aims.ac.za)
- **Supervisor**: Dr. Michael J. Winckler (Heidelberg University, Germany)




