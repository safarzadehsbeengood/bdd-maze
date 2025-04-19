from cell import Cell
import random
import time

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
        self.create_cells()

    def create_cells(self):
        for i in range(self._n):
            row = []
            for j in range(self._m):
                cell = Cell(self._win) 
                row.append(cell)
            self._cells.append(row)
        # for i in range(self._n):
            # for j in range(self._m):
                # self.draw_cell(i, j)
        self._break_entrance_and_exit()
        self._animate()

    def draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._x1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)

    def _animate(self):
        if self._win is None:
            return
        for i in range(self._n):
            for j in range(self._m):
                self.draw_cell(i, j)
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top = False
        self._cells[self._n-1][self._m-1].bottom = False