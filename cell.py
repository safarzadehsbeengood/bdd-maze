from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self.right = True
        self.left = True
        self.top = True
        self.bottom = True

        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        # x1, y1 is top left corner
        # x2, y2 is bottom right corner

        color = self.left
        color = "black" if self.left else "white"
        if self.left:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, color)
            
        color = "black" if self.top else "white"
        if self.top:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, color)

        color = "black" if self.bottom else "white"
        if self.bottom:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, color)

        color = "black" if self.right else "white"
        if self.right:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, color)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        ax, ay = (self._x1+self._x2)//2, (self._y1+self._y2)//2
        bx, by = (to_cell._x1+to_cell._x2)//2, (to_cell._y1+to_cell._y2)//2
        line = Line(Point(ax, ay), Point(bx, by))
        self._win.draw_line(line, "gray" if undo else "red")
