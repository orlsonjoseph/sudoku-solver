from math import sqrt

class Sudoku:
    def __init__(self, grid):
        self.grid = grid

        self.M = len(self.grid)
        self.N = int(sqrt(self.M))

    def is_legal(self, row, col, num):
        for x in range(self.M):
            if self.grid[row][x] == num:
                return False

            if self.grid[x][col] == num:
                return False

        s_row = row - row % 3
        s_col = col - col % 3
        
        for x in range(self.N):
            for y in range(self.N):
                if self.grid[x + s_row][y + s_col] == num:
                    return False
        return True

    def solve(self, row, col):
        if row == self.M - 1 and col == self.M:
            return True

        if col == self.M:
            row += 1; col = 0

        if self.grid[row][col] == 0:
            for candidate in range(1, self.M + 1):
                if self.is_legal(row, col, candidate):
                    self.grid[row][col] = candidate

                    if self.solve(row, col + 1):
                        return True
                self.grid[row][col] = 0
        else:
            return self.solve(row, col + 1)

        return False

    def __repr__(self):
        output = ""

        for i in range(self.M):
            for j in range(self.M):
                output += str(self.grid[i][j]) + " "
            output += "\n"

        return output

if __name__ == "__main__":
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solution = Sudoku(grid)

    if solution.solve(0, 0):
        print(solution)

    else:
        print("No solution found")
