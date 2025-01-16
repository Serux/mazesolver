from tkinter import Tk, BOTH, Canvas

import shapes.Line as l
import shapes.Point as p

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.rw= Tk()
        self.rw.title("Title")
        self.canvas = Canvas()
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
        
        
def main():
    win = Window(800, 600)
    
    p1 = p.Point(0,0)
    p2 = p.Point(100,100)
    l1 = l.Line(p1,p2)
    win.draw_line(l1,"red")
    
    win.wait_for_close()   
    
    
main()