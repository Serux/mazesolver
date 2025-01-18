from tkinter import Tk, BOTH, Canvas

from shapes import Cell
from shapes import Line
from shapes import Point
from shapes import Maze



class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.rw= Tk()
        self.rw.title("Title")
        self.canvas = Canvas(height=self.height,width=self.width)
        self.canvas.pack()
        self.is_running= False
        self.rw.protocol("WM_DELETE_WINDOW",self.close)
    def redraw(self):
        self.rw.update_idletasks()
        self.rw.update()
    def wait_for_close(self):
        self.is_running = True
        while(self.is_running):
            self.redraw()
    def close(self):
        self.is_running = False
    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)
    def draw_cell(self,cell,fill_color):
        cell.draw(fill_color)
        
        
def main():
    win = Window(800, 600)
    
    m = Maze(5,5,30,30,10,10,win) 

    m.solve()
    
    win.wait_for_close()   
    
    
main()