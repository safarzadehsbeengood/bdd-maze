from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__window  = Canvas(self.__root, bg='white', width=width, height=height)
        self.__window.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill="black"):
        line.draw(self.__window, fill)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        
    def draw(self, canvas, fill="black"):
        x1, y1 = self.a.x, self.a.y
        x2, y2 = self.b.x, self.b.y
        canvas.create_line(x1, y1, x2, y2, fill=fill, width=2)