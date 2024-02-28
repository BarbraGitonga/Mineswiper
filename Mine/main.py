from tkinter import *
import settings as st

root = Tk()
root.configure(bg="grey")
root.geometry(f'{st.WIDTH}x{st.HEIGHT}') #size of window
root.title("Minesweeper") #title
root.resizable(False, False) #disables the maximize button on window

top_frame = Frame(
    root,
    bg='black',
    width= 720,
    height=45,
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = 'white',
    width=100,
    height=315,
)
left_frame.place(x=0, y=45)

#Run the window
root.mainloop() # opens window
