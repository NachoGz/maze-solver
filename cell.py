from point import Point
from line import Line
class Cell():
    def __init__(self, x1, x2, y1, y2, win=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
            if self._win is None:
                return
            x1 = self._x1 
            x2 = self._x2 
            y1 = self._y1 
            y2 = self._y2 
            if self.has_left_wall:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line)
            else:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line, "white")
            if self.has_top_wall:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line)
            else:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line, "white")
            if self.has_right_wall:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line)
            else:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line, "white")
            if self.has_bottom_wall:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line)
            else:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line, "white")

    def get_center(self):
        cx = (self._x1 + self._x2) / 2
        cy = (self._y1 + self._y2) / 2
        return Point(cx, cy)

    def draw_move(self, to_cell, undo=False):
        from_center = self.get_center()
        to_center = to_cell.get_center()
        path = Line(from_center, to_center)
        if undo:
            self._win.draw_line(path, "gray")
        else:
            self._win.draw_line(path, "red")
