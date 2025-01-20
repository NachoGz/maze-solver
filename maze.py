from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                # position of the cell
                x1 = self.__x1 + j * self.__cell_size_x
                y1 = self.__y1 + i * self.__cell_size_y
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y

                cell = Cell(x1, x2, y1, y2, self.__win)
                row.append(cell)
            self._cells.append(row)
        
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]

        cell.draw()

        self._animate()

    def _animate(self):
        self.__win.redraw()

        time.sleep(0.05)
    



            