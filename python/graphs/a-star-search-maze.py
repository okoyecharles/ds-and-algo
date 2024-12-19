import math
import random
import os
import time


class Cell:
    def __init__(self, value, row, col, g=float("inf")):
        self.value = value
        self.row = row
        self.col = col
        self.g = g
        self.prev: Cell = None

    def calc_h(self, goal_pos: (int, int)):
        gr, gc = goal_pos
        r, c = self.row, self.col
        h = math.sqrt((r - gr) * (r - gr) + (c - gc) * (c - gc))
        return h


class Maze:
    def __init__(self, walls=True, dims=(12, 12), walls_probability=0.4):
        self.ROWS = dims[0]
        self.COLS = dims[1]
        self.maze = [
            [Cell("empty", row, col) for col in range(self.COLS)]
            for row in range(self.ROWS)
        ]

        if walls:
            for row in range(self.ROWS):
                for col in range(self.COLS):
                    if random.random() < walls_probability:
                        self.maze[row][col].value = "wall"
            self.maze[0][0].value = "empty"
            self.maze[self.ROWS - 1][self.COLS - 1].value = "empty"

    def visualize(self):
        char_map = {
            "empty": " .",
            "wall": " ⨁",
            "closed": " +",
            "open": " -",
            "path": " ▧",
        }
        for row in range(self.ROWS):
            for col in range(self.COLS):
                cell = self.maze[row][col]
                print(char_map[cell.value], end="")
            print()

    def generate_path(self, goal_cell: Cell):
        curr_cell = goal_cell
        curr_cell.value = "path"
        path_count = 1
        while curr_cell.prev:
            curr_cell.prev.value = "path"
            curr_cell = curr_cell.prev
            path_count += 1
        return path_count


def get_neighbors(cell: Cell, maze, closed, diagonal):
    ROWS, COLS = len(maze), len(maze[0])
    r, c = cell.row, cell.col
    steps = ( 
        [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        if diagonal
        else [(0, 1), (1, 0), (0, -1), (-1, 0)]
    )
    neighbors = []
    for dr, dc in steps:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
            continue

        neighbor = maze[nr][nc]
        if neighbor not in closed:
            neighbors.append(neighbor)
    return neighbors


def get_fit_cell(set, goal_pos):
    minimum_fitness_number = float("inf")
    minimum_fitness_cell = None

    for cell in set:
        if minimum_fitness_cell == None:
            minimum_fitness_cell = cell
            minimum_fitness_number = cell.g + cell.calc_h(goal_pos)
        else:
            cell_fitness_number = cell.g + cell.calc_h(goal_pos)
            if cell_fitness_number < minimum_fitness_number:
                minimum_fitness_cell = cell
                minimum_fitness_number = cell_fitness_number
    return minimum_fitness_cell


def a_star(maze, start, end, diagonal=False):
    sr, sc = start[0], start[1]
    er, ec = end[0], end[1]
    start_cell = maze.maze[sr][sc]
    start_cell.g = 0
    open = {start_cell}
    closed = set()

    while len(open) > 0:
        fit_cell = get_fit_cell(open, end)
        open.remove(fit_cell)
        fit_cell.value = "empty"

        if fit_cell.row == end[0] and fit_cell.col == end[1]:
            fit_cell.value = "closed"
            path_steps = maze.generate_path(fit_cell)
            maze.visualize()
            print("\nPath found:", path_steps, "steps")
            return fit_cell

        neighbors = get_neighbors(fit_cell, maze.maze, closed, diagonal=diagonal)
        for neighbor in neighbors:
            if neighbor.value == "wall":
                continue

            if neighbor not in open or fit_cell.g + 1 < neighbor.g:
                neighbor.g = 1 + fit_cell.g
                neighbor.prev = fit_cell
                if neighbor not in open:
                    neighbor.value = "open"
                    open.add(neighbor)

        fit_cell.value = "closed"
        closed.add(fit_cell)
        maze.visualize()
        time.sleep(0.02)
        os.system("clear")

    maze.visualize()
    print("\nNo path found")


m_dims = (15, 15)
m = Maze(dims=m_dims, walls_probability=0.75)
a_star(m, (0, 0), (m_dims[0] - 1, m_dims[1] - 1))
