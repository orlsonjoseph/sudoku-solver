# Sudoku Solver

This repository contains a Sudoku solver implemented in Python. The solver is designed to solve Sudoku puzzles of various difficulties.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Sudoku is a popular puzzle game that involves filling a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 sub-grids contains all of the digits from 1 to 9.

This Sudoku solver is implemented in Python and aims to solve Sudoku puzzles automatically. It uses a backtracking algorithm to systematically fill in the empty cells of a given Sudoku grid until a solution is found.

## Installation

To use this Sudoku solver, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/orlsonjoseph/sudoku-solver.git`.
2. Navigate to the cloned directory: `cd sudoku-solver`.

## Usage

To solve a Sudoku puzzle using this solver, you can use the following steps:

1. Open the `solver.py` file in a Python editor or IDE.
2. Modify the `grid` variable at the bottom of the file to represent the unsolved Sudoku puzzle you want to solve. Use `0` to represent empty cells.
3. Run the `solver.py` script.
4. The solver will attempt to solve the puzzle and print the solution if found.

## Algorithm

The Sudoku solver in this repository uses a backtracking algorithm to find the solution to a Sudoku puzzle. The algorithm works as follows:

1. Find the next empty cell in the grid.
2. If there are no empty cells, the puzzle is solved.
3. Try each number from 1 to 9 in the empty cell.
4. If a number is valid in the current position, place it in the cell.
5. Recursively repeat the process for the next empty cell.
6. If a number is not valid, backtrack to the previous cell and try the next number.
7. If all numbers have been tried and none is valid, backtrack further.
8. Repeat the process until a solution is found or all possibilities have been exhausted.

## Contributing

Contributions to this Sudoku solver repository are always welcome. If you find a bug or have suggestions for improvements, please open an issue or submit a pull request. Together, we can make the solver even better!

## License

This Sudoku solver is released under the MIT License. Feel free to use, modify, and distribute the code as permitted by the license.
