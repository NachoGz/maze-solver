from point import Point
from line import Line
class Cell():
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win

    def draw(self):
        top_left_corner = Point(self.__x1, self.__y1)
        bottom_left_corner = Point(self.__x1, self.__y2)
        top_right_corner = Point(self.__x2, self.__y1)
        bottom_right_corner = Point(self.__x2, self.__y2)

        if self.has_left_wall:
            wall = Line(top_left_corner, bottom_left_corner)
            self.__win.draw_line(wall, "black")
        if self.has_right_wall:
            wall = Line(top_right_corner, bottom_right_corner)
            self.__win.draw_line(wall, "black")
        if self.has_top_wall:
            wall = Line(top_left_corner, top_right_corner)
            self.__win.draw_line(wall, "black")
        if self.has_bottom_wall:
            wall = Line(bottom_left_corner, bottom_right_corner)
            self.__win.draw_line(wall, "black")

    def get_center(self):
        cx = (self.__x1 + self.__x2) / 2
        cy = (self.__y1 + self.__y2) / 2
        return Point(cx, cy)

    def draw_move(self, to_cell, undo=False):
        from_center = self.get_center()
        to_center = to_cell.get_center()
        path = Line(from_center, to_center)
        if undo:
            self.__win.draw_line(path, "gray")
        else:
            self.__win.draw_line(path, "red")
            