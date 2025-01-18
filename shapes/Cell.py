from . import Line
from . import Point


class Cell:
    def __init__(self,x1,y1,x2,y2,win=None,has_left_wall=True,has_right_wall=True,has_top_wall=True,has_bottom_wall=True,):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False
    
    def __str__(self):
        return "Cell()"
    
    def middlePoint(self):
        mx = self._x1 + ((self._x2 - self._x1) /2)
        my = self._y1 + (self._y2 - self._y1) /2
        return Point(mx,my)
        
    def draw(self,fill_color):
       
        p1 = Point(self._x1,self._y1)
        p2 = Point(self._x1,self._y2)
        l1 = Line(p1,p2)
        if (self._win):
            l1.draw(self._win.canvas,fill_color if self.has_left_wall else "#d9d9d9")
        
        p1 = Point(self._x2,self._y1)
        p2 = Point(self._x2,self._y2)
        l1 = Line(p1,p2)
        if (self._win):
            l1.draw(self._win.canvas,fill_color if self.has_right_wall else "#d9d9d9")
       
        p1 = Point(self._x1,self._y1)
        p2 = Point(self._x2,self._y1)
        l1 = Line(p1,p2)
        if (self._win):
            l1.draw(self._win.canvas,fill_color if self.has_top_wall else "#d9d9d9")
    
        p1 = Point(self._x1,self._y2)
        p2 = Point(self._x2,self._y2)
        l1 = Line(p1,p2)
        if (self._win):
            l1.draw(self._win.canvas,fill_color if self.has_bottom_wall else "#d9d9d9")
            
    def draw_move(self,to_cell, undo=False):
        p1 = self.middlePoint()
        #print(p1)
        p2 = to_cell.middlePoint()
        #print(p2)
        
        l1 = Line(p1,p2)
        color = "red" if not undo else "gray"
        l1.draw(self._win.canvas,color)
        
        