from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        """_summary_

        Args:
            is_mine (bool, optional): _description_. Defaults to False.
        """
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        """_summary_

        Args:
            location (_type_): _description_
        """
        btn = Button(
            location,
            text='Text'
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