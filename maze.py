from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, animate=True, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self.animate = animate
        self.seed = seed
        self._create_cells()
        if seed:
            random.seed(seed)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                # position of the cell
                x1 = self.__x1 + j * self.__cell_size_x
                y1 = self.__y1 + i * self.__cell_size_y
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                                
                cell = Cell(x1, x2, y1, y2, self.__win)
                
                row.append(cell)
            self._cells.append(row)
        
        for row in range(self._num_rows):
            for col in range(self._num_cols):
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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].has_right_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # right
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
            # up
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # down
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_i, next_j = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_j == j:
                self._cells[i][j].has_right_wall = False
                self._cells[i][next_j].has_left_wall = False
            # left
            if next_j < j:
                self._cells[i][j].has_left_wall = False
                self._cells[i][next_j].has_right_wall = False
            # down
            if next_i > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][j].has_top_wall = False
            # up
            if next_i < i:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][j].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if (i, j) == (self._num_rows - 1, self._num_cols - 1):
            return True

        # next_index_list = []

        # determine which cell(s) to visit next
        # left
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_left_wall:
            # next_index_list.append((i, j - 1))
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        # right
        if j < self._num_cols - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_right_wall:
            # next_index_list.append((i, j + 1))
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        # up
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_top_wall:
            # next_index_list.append((i - 1, j))
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        # down
        if i < self._num_rows - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_bottom_wall:
            # next_index_list.append((i + 1, j))
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        
        return False



        