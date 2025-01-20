from cell import Cell
import time
import random
from point import Point
from line import Line

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, animate=True, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self.animate = animate
        self.seed = seed
        self._create_cells()
        if seed:
            random.seed(seed)
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                # position of the cell
                x1 = self.__x1 + j * self.__cell_size_x
                y1 = self.__y1 + i * self.__cell_size_y
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                
                # entrance
                if i == 0 and j == 0:
                    cell = Cell(x1, x2, y1, y2, self.__win, has_top_wall=False)
                # exit
                elif i == (self.num_rows-1) and j == (self.num_cols-1):
                    cell = Cell(x1, x2, y1, y2, self.__win, has_bottom_wall=False)
                else:
                    cell = Cell(x1, x2, y1, y2, self.__win)
                
                row.append(cell)
            self._cells.append(row)
        
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]

        cell.draw()

        if self.animate:
            self._animate()

    def _animate(self):
        if self.__win:
            self.__win.redraw()

        time.sleep(0.05)

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]

        cell.visited = True
        x1 = cell.get_top_left_x()
        x2 = cell.get_bottom_right_x()
        y1 = cell.get_top_left_y()
        y2 = cell.get_bottom_right_y()

        top_left_corner = Point(x1, y1)
        bottom_left_corner = Point(x1, y2)
        top_right_corner = Point(x2, y1)
        bottom_right_corner = Point(x2, y2)
        
        while True:
            to_visit = []
            try:
                adj_cell_r = self._cells[i][j+1] # right
                if not adj_cell_r.visited:
                    to_visit.append((i, j+1))
            except IndexError:
                adj_cell_r = None
            try:
                adj_cell_l = self._cells[i][j-1] # left
                if not adj_cell_l.visited:
                    to_visit.append((i, j-1))
            except IndexError:
                adj_cell_l = None
            try:
                adj_cell_u = self._cells[i-1][j] # up
                if not adj_cell_u.visited:
                    to_visit.append((i-1, j))
            except IndexError:
                adj_cell_u = None
            try:
                adj_cell_d = self._cells[i+1][j] # down
                if not adj_cell_d.visited:
                    to_visit.append((i+1, j))
            except IndexError:
                adj_cell_d = None

            if not to_visit:
                cell.draw()
                return
            else:
                direction = random.choice(to_visit)
                # determine the wall
                if j+1 == direction[1]:
                    right_wall = Line(top_right_corner, bottom_right_corner)
                    self.__win.draw_line(right_wall, "white")
                elif j-1 == direction[1]:
                    left_wall = Line(top_left_corner, bottom_left_corner)
                    self.__win.draw_line(left_wall, "white")
                elif i+1 == direction[0]:
                    top_wall = Line(top_left_corner, top_right_corner)
                    self.__win.draw_line(top_wall, "white")
                elif i-1 == direction[0]:
                    bottom_wall = Line(bottom_left_corner, bottom_right_corner)
                    self.__win.draw_line(bottom_wall, "white")

                # move to the chosen cell
                self._break_walls_r(direction[0], direction[1])
