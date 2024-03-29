from tkinter import Button, Label
import random
import settings as st
import ctypes
import sys
class Cell:
    all = []
    cell_count_label_object = None
    cell_count = st.CELL_COUNT

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.is_mine_candidate = False
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
            if self.surrounding_mines == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == st.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations', 'You won the game!', 0)
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg = 'black',
            fg = 'white',
            text=f"Cells left:{Cell.cell_count}",
            # width = 9,
            # height = 2,
            font=("", 12)
        )
        Cell.cell_count_label_object = label
        
    
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
        if not self.is_opened:
            Cell.cell_count-=1
            self.cell_btn_object.configure(text=self.surrounding_mines)
            # Replace the text of the cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells left:{Cell.cell_count}")
                #if this was a mine candidate then fior saferty we should configure the background color to system button face
                self.cell_btn_object.configure(
                    bg = 'systemButtonFace'
                )
        #Mark cell as opened
            self.is_opened=True

    def show_mine(self):
        # a logic to carry out interrupt that the player has lost
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game over', 0)
        sys.exit()

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        mines = random.sample(
            Cell.all, st.MINES_COUNT
        )
        for mine in mines:
            mine.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"