from logging import RootLogger
from pickle import FRAME
from tkinter import *
import settings as st
import utils

root = Tk()
root.configure(bg="grey")
root.geometry(f'{st.WIDTH}x{st.HEIGHT}') #size of window
root.title("Minesweeper") #title
root.resizable(False, False) #disables the maximize button on window

top_frame = Frame(
    root,
    bg='black',
    width= utils.width_prct(100),
    height=utils.height_prct(12.5),
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = 'white',
    width=utils.width_prct(15),
    height=utils.height_prct(100),
)
left_frame.place(x=0, y=45)

center_frame = Frame(
    root,
    bg='grey',
    width = utils.width_prct(85),
    height = utils.height_prct(86.5)
)
center_frame.place(x=utils.width_prct(15), y=utils.height_prct(12.5))
#Run the window
root.mainloop() # opens window
