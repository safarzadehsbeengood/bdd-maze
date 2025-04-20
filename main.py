from graphics import Window, Button
from maze import Maze

num_rows = 30
num_cols = 50
margin = 50
screen_x = 1200
screen_y = 800
cell_size_x = (screen_x - 2 * margin) / num_cols
cell_size_y = (screen_y - 2 * margin) / num_rows

def main():
    win = Window(screen_x, screen_y)
    def generate_maze():
        return Maze(
            margin, 
            margin, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win
        )

    maze = generate_maze()
    maze.solve()
    win.wait_for_close()

main()