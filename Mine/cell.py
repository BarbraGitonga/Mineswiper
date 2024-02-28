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
        self.cell_btn_object = btn