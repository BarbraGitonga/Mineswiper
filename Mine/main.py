from tkinter import *
import settings as st
from utils import width_prct, height_prct
from cell import Cell

root = Tk()
root.configure(bg="grey")
root.geometry(f'{st.WIDTH}x{st.HEIGHT}') #size of window
root.title("Minesweeper") #title
root.resizable(False, False) #disables the maximize button on window

top_frame = Frame(
    root,
    bg='black',
    width= width_prct(100),
    height=height_prct(12.5),
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = 'white',
    width=width_prct(15),
    height=height_prct(100),
)
left_frame.place(x=0, y=45)

center_frame = Frame(
    root,
    bg='grey',
    width = width_prct(85),
    height = height_prct(86.5)
)
center_frame.place(
    x=width_prct(15),
    y=height_prct(12.5)
)

for x in range(st.GRID_SIZE):
    for y in range(st.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=y, row=x)

print(Cell.all)

#Run the window
root.mainloop() # opens window
