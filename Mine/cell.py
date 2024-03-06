from cgitb import text
from tkinter import Button
import random
import settings as st
class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=9,
            height=2,
        )
        btn.bind('<Button-1>', self.left_click_action) # left click
        btn.bind('<Button-3>', self.right_click_action) # right click
        self.cell_btn_object = btn

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
    
    def get_cell_by_axis(self, x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property       
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x -1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x -1, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1)
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_mines(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounding_mines)
    
    def show_mine(self):
        # a logic to carry out interrupt thatthe player has lost
        self.cell_btn_object.configure(bg='red')

    def right_click_action(self, event):
        print(event)
        print("right click action")

    @staticmethod
    def randomize_mines():
        mines = random.sample(
            Cell.all, st.MINES_COUNT
        )
        for mine in mines:
            mine.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"