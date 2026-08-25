
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")

# template to create a ctk window
class Window(ctk.CTk, tk.Tk):
    def __init__(self, width, height):
        super().__init__()

        # scale attributes
        self.geo_width = width
        self.geo_height = height

        self.geometry(f"{self.geo_width}x{self.geo_height}")

        # switch / set icon
        self.set_icon(tk.PhotoImage(file = "/home/crane/Pictures/BoxIcon.png"))
        self.title("Nonogram")

    def set_icon(self, icon_path):
        self.wm_iconphoto(False, icon_path)


# template to create a ctk button
class Box(ctk.CTkButton):
    def __init__(self, width, height, r, c):

        # attributes
        # geometry
        self.box_width = width
        self.box_height = height

        # grid positioning
        self.row = r
        self.column = c
        # grid style
        self.grid_space = 2
        self.border_colour = '#303030'

        # colours
        self.box_colour = '#d6d6d6'
        self.back_colour = '#303030'
        self.hover = '#c2c2c2'

        # instantiate a Box using ctk button super class
        super().__init__(grid, width = self.box_width, height = self.box_height, text = '',
        fg_color = self.box_colour, bg_color = self.back_colour, hover_color = self.hover, 
        border_width = self.grid_space, border_color = self.border_colour, command = self.switch)
        # place in grid format
        super().grid(row = self.row, column = self.column)

    # toggle between Box states (select)
    def switch(self):
        # colour map to states in format: {'BOX':['HOVER'], ...}
        box_colour_map = {'#d6d6d6': ['#c2c2c2'], '#424242': ['#525252']}
        box_colours = list(box_colour_map)
        if self.box_colour == box_colours[0]:
            set_box_colour = box_colours[1]
            set_hover_colour = box_colour_map[set_box_colour][0]
        else:
            set_box_colour = box_colours[0]
            set_hover_colour = box_colour_map[set_box_colour][0]
        # configure instance's colour attributes
        self.box_colour = set_box_colour
        self.configure(fg_color = set_box_colour, hover_color = set_hover_colour)


# 
class Set():
    def __init__(self, scale):
        
        self.scale = scale
    
    def place_set(self):
        for r in range(self.scale):
            for c in range(self.scale):
                box = Box(60, 60, r, c)


# template to create a ctk Frame for a grid of Boxes
class Grid(ctk.CTkFrame):
    def __init__(self, master, width, height, radius, place_x, place_y, colour):

        # attributes
        # parent object
        self.master = master

        # geometric properties
        self.frame_width = width
        self.frame_height = height
        self.c_radius = radius

        # colours
        self.back_colour = colour

        # placement
        self.x = place_x
        self.y = place_y

        # instantiate the ctk frame object
        super().__init__(master, width = self.frame_width, height = self.frame_height, 
        fg_color = self.back_colour)
        # place in window using x, y coordinates
        super().place(x = self.x, y = self.y)


window = Window(600, 600)
grid = Grid(window, 540, 540, 2, 10, 10, '#ffffff')

set1 = Set(2)
set1.place_set()

# event loop
window.mainloop()