from window import Window
from cell import Cell
from line import Line
from point import Point
from maze import Maze

def main():
    # win = Window(800, 600)

    # # Test Cell 1: Fully enclosed cell
    # cell1 = Cell(x1=100, y1=100, x2=300, y2=300, win=win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True)
    # cell1.draw()

    # # # Test Cell 2: Cell with no walls
    # cell2 = Cell(x1=350, y1=100, x2=550, y2=300, win=win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True)
    # cell2.draw()

    # cell1.draw_move(cell2, undo=False)

    # Draw a move from cell2 back to cell1 (undo)
    # cell2.draw_move(cell1, undo=True)

    # test maze
    # Define maze parameters
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()

if __name__ == '__main__':
    main()
