
import tkinter as tk
import customtkinter as ctk



#
class Window(ctk.CTk, tk.Tk):
    def __init__(self, width, height):
        super().__init__()

        # scale
        self.geo_width = width
        self.geo_height = height

        self.geometry(f"{self.geo_width}x{self.geo_height}")

        # switch / set icon
        self.set_icon(tk.PhotoImage(file = "/home/crane/Pictures/BoxIcon.png"))
        self.title("Nonogram")

    def set_icon(self, icon_path):
        self.wm_iconphoto(False, icon_path)


#
class Box(ctk.CTkButton):
    def __init__(self, width, height, r, c):

        self.box_width = width
        self.box_height = height

        self.row = r
        self.column = c

        self.grid_space = 2
        self.border_colour = '#303030'

        self.box_colour = '#d6d6d6'
        self.back_colour = '#303030'
        self.hover = '#c2c2c2'

        super().__init__(grid, width = self.box_width, height = self.box_height, text = '',
        fg_color = self.box_colour, bg_color = self.back_colour, hover_color = self.hover, 
        border_width = self.grid_space, border_color = self.border_colour)
        super().grid(row = self.row, column = self.column)


#
class Grid(ctk.CTkFrame):
    def __init__(self, master, width, height, radius, place_x, place_y, colour):

        self.master = master

        # properties
        self.frame_width = width
        self.frame_height = height
        self.c_radius = radius
        self.back_colour = colour

        self.x = place_x
        self.y = place_y

        super().__init__(master, width = self.frame_width, height = self.frame_height, 
        fg_color = self.back_colour)
        super().place(x = self.x, y = self.y)


window = Window(600, 600)
grid = Grid(window, 540, 540, 2, 10, 10, '#ffffff')

box = Box(60, 60, 0, 0)
box2 = Box(60, 60, 0, 1)
box3 = Box(60, 60, 1, 0)
box4 = Box(60, 60, 1, 1)
box5 = Box(60, 60, 2, 0)
box6 = Box(60, 60, 2, 1)

box7 = Box(60, 60, 0, 2)
box8 = Box(60, 60, 0, 3)
box9 = Box(60, 60, 1, 2)
box10 = Box(60, 60, 1, 3)
box11 = Box(60, 60, 2, 2)
box12 = Box(60, 60, 2, 3)

# event loop
window.mainloop()