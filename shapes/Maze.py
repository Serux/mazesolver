import random
import time

from . import Cell


class Maze:
    def __init__(self, x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win =None, seed = None):
        if  seed == None:
            random.seed(seed)
            
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        if(i == self.num_rows-1 and j == self.num_cols -1):
            return True
        ##if(i+1 == self.num_rows-1 and j == self.num_cols -1):
        ##    return True
        #if(i == self.num_rows-1 and j+1 == self.num_cols -1):
        #    return True
        
        self._animate()
        self._cells[i][j].visited = True
        
        if(i>0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_top_wall ):
            #up
            self._cells[i][j].draw_move(self._cells[i-1][j])
            fin = self._solve_r(i-1,j)
            if(fin):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j],True)
            
        if(i<self.num_rows-1 and not self._cells[i+1][j].visited and not self._cells[i][j].has_bottom_wall ):
            #down
            self._cells[i][j].draw_move(self._cells[i+1][j])
            fin = self._solve_r(i+1,j)
            if(fin):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j],True)
        if(j>0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_left_wall ):
            #right
            self._cells[i][j].draw_move(self._cells[i][j-1])
            fin = self._solve_r(i,j-1)
            if(fin):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1],True)
        if(j<self.num_cols-1 and not self._cells[i][j+1].visited and not self._cells[i][j].has_right_wall ):
            #left
            self._cells[i][j].draw_move(self._cells[i][j+1])
            fin = self._solve_r(i,j+1)
            if(fin):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1],True)
            
        return False
        
        
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            column = []
            for j in range(self.num_cols):
                x1 = self.x1 + self.cell_size_x*j
                y1 = self.y1 + self.cell_size_y*i
                x2 = self.x1 + self.cell_size_x*j + self.cell_size_x
                y2 = self.y1 + self.cell_size_y*i + self.cell_size_y
                c = Cell(x1,y1,x2,y2,self.win)
                column.append(c)
                self._draw_cell(c)
            self._cells.append(column)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
       
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        
        self._draw_cell(self._cells[self.num_rows-1][self.num_cols-1])
        
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
       
        while True:
            toVisit = []
            if(i>0 and not self._cells[i-1][j].visited ):
                #down
                toVisit.append((i-1,j))
            if(i<self.num_rows-1 and not self._cells[i+1][j].visited ):
                #up
                toVisit.append((i+1,j))
            if(j>0 and not self._cells[i][j-1].visited ):
                #right
                toVisit.append((i,j-1))
            if(j<self.num_cols-1 and not self._cells[i][j+1].visited ):
                #left
                toVisit.append((i,j+1))
            if(len(toVisit) == 0):
                self._draw_cell(self._cells[i][j])
                return
            randi = random.randrange(len(toVisit))
            i1, j1 = toVisit[randi]
            if(i1 < i):
                self._cells[i][j].has_top_wall = False
                self._cells[i1][j1].has_bottom_wall = False
            if(i1 > i):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i1][j1].has_top_wall = False
            if(j1 < j):
                self._cells[i][j].has_left_wall = False
                self._cells[i1][j1].has_right_wall = False
            if(j1 > j):
                self._cells[i][j].has_right_wall = False
                self._cells[i1][j1].has_left_wall = False
            self._break_walls_r(i1,j1)
                
            
            
            
    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False
            
    def _draw_cell(self,cell):
        cell.draw("black") 
        self._animate()
    def _animate(self):
        if(self.win):
            self.win.redraw()
            time.sleep(0.00001)
        
    
        
        
        