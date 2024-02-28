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
        print(event)
        print("left click action")

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