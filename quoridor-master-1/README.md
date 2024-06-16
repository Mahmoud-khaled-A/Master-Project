```markdown
# Quoridor Strategy Master Project

## Overview
This repository contains the code and documentation for the project titled **"Mathematical Modelling and Implementation of Game Strategy for the Board Game Quoridor"**. The project explores various algorithms to develop strategies for mastering the board game Quoridor. The algorithms implemented include Minimax with Alpha-Beta Pruning (ABP), Expectimax (EM), and Monte Carlo Tree Search (MCTS), with the addition of probabilistic decision-making using the Softmax function.

## Contents
- **Source Code**: Implementation of the Quoridor game and the algorithms.
- **Documentation**: Detailed explanation of the project, methodologies, and findings.
- **Results**: Data and analysis from the experiments comparing different algorithms.

## Project Structure
```
quoridor-master-1/
├── src/
│   ├── quoridor.py
│   ├── algorithms/
│   │   ├── minimax_abp.py
│   │   ├── expectimax.py
│   │   ├── mcts.py
│   ├── utils/
│   │   ├── board_notation.py
│   │   ├── game_rules.py
│   │   ├── softmax.py
├── data/
│   ├── experiment_results.csv
│   ├── plots/
│   │   ├── win_rate_comparison.png
│   │   ├── execution_time_analysis.png
├── docs/
│   ├── project_report.pdf
│   ├── readme.md
└── README.md
```

## Installation
To run the project, clone the repository and install the required dependencies:
```sh
git clone https://github.com/TheMathematicianMahmoud/Master-Project.git
cd Master-Project/quoridor-master-1
pip install -r requirements.txt
```

## Usage
To start the Quoridor game with a specific algorithm, run the following command:
```sh
python src/quoridor.py --algorithm [algorithm_name]
```
Replace `[algorithm_name]` with one of the following options:
- `minimax_abp`
- `expectimax`
- `mcts`

## Algorithms
### Minimax with Alpha-Beta Pruning (ABP)
The Minimax algorithm is a decision-making tool for two-player zero-sum games. Alpha-Beta Pruning optimizes the Minimax algorithm by pruning unnecessary branches, making it more efficient.

### Expectimax (EM)
The Expectimax algorithm extends Minimax to handle probabilistic scenarios. It calculates expected values for each decision, considering the probability distribution of possible opponent moves.

### Monte Carlo Tree Search (MCTS)
MCTS is a heuristic search algorithm combining precision tree searching with exploratory random sampling. It balances exploration and exploitation to find optimal moves.

### Softmax Function
The Softmax function introduces randomness in decision-making, preventing repetitive patterns and exploring a wider range of game states.

## Results
The project evaluates the performance of the algorithms based on win rates, execution times, and strategic depth in various game scenarios. The findings indicate that ABP is the most efficient but still lacks against human players. Detailed results and analysis can be found in the `docs/project_report.pdf` file.

## Contributors
- **Mahmoud Khaled Abdelkader** (mahmoudkh@aims.ac.za)
- **Supervisor**: Dr. Michael J. Winckler (Heidelberg University, Germany)

## License
This project is licensed under the MIT License.
```
