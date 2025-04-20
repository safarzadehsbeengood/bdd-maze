from cell import Cell
import random
import time

LEFT, RIGHT, UP, DOWN = (-1, 0), (1, 0), (0, 1), (0, -1)
DIRECTIONS = [UP, DOWN, RIGHT, LEFT]

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._m = num_rows
        self._n = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self.create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def create_cells(self):
        for i in range(self._n):
            row = []
            for j in range(self._m):
                cell = Cell(self._win) 
                row.append(cell)
            self._cells.append(row)
        for i in range(self._n):
            for j in range(self._m):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._x1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        # self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top = False
        self._cells[self._n-1][self._m-1].bottom = False
        self._draw_cell(0, 0)
        self._draw_cell(self._n-1, self._m-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._n - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._m - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].right = False
                self._cells[i + 1][j].left = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].left = False
                self._cells[i - 1][j].right = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].bottom = False
                self._cells[i][j + 1].top = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].top = False
                self._cells[i][j - 1].bottom = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
            
    def _reset_cells_visited(self):
        for i in range(self._n):
            for j in range(self._m):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        print(i, j)
        self._animate()
        curr = self._cells[i][j]
        curr.visited = True
        if i == self._n-1 and j == self._m-1:
            return True 
        # right
        if i + 1 < self._n and not self._cells[i+1][j].visited and not curr.right:
            if self._solve_r(i+1, j):
                curr.draw_move(self._cells[i+1][j])
                return True
            else:
                curr.draw_move(self._cells[i+1][j], True)

        # left
        if i - 1 >= 0 and not self._cells[i-1][j].visited and not curr.left:
            if self._solve_r(i-1, j):
                curr.draw_move(self._cells[i-1][j])
                return True
            else:
                curr.draw_move(self._cells[i-1][j], True)
        # up 
        if j - 1 >= 0 and not self._cells[i][j-1].visited and not curr.top:
            if self._solve_r(i, j-1):
                curr.draw_move(self._cells[i][j-1])
                return True
            else:
                curr.draw_move(self._cells[i][j-1], True)
        # down
        if j < self._m and not self._cells[i][j+1].visited and not curr.bottom:
            if self._solve_r(i, j+1):
                curr.draw_move(self._cells[i][j+1])
                return True
            else:
                curr.draw_move(self._cells[i][j+1], True)

        return False