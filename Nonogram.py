
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
        self.set_icon(tk.PhotoImage(file = "/home/crane/Pictures/Google Icons/BoxIcon.png"))
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
        self.grid_space = 0
        self.border_colour = '#303030'

        # colours
        self.box_colour = '#d6d6d6'
        self.back_colour = '#303030'
        self.hover = '#c2c2c2'

        # instantiate a Box using ctk button super class
        super().__init__(grid, width = self.box_width, height = self.box_height, text = '',
        corner_radius = 0, fg_color = self.box_colour, bg_color = self.back_colour, 
        hover_color = self.hover, border_width = self.grid_space, 
        border_color = self.border_colour, command = self.switch)
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


# template to create a grid of Boxes
class Set():
    def __init__(self, scale):
        
        # attributes
        # define a set
        self.set_list = []
        
        # scale property
        self.scale = scale
        # call place set method to display
        self.place_set()
    
    # creates the set to reflect input scale
    def place_set(self):
        for r in range(self.scale):
            contents = []
            for c in range(self.scale):
                box = Box(60, 60, r, c)
                contents.append(box)
            self.set_list.append(contents)

    # prints list of set objects into terminal
    def print_set(self):
        print(self.set_list)


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


# template to create a ctk Label for corresponding box patterns
class Label(ctk.CTkLabel):
    def __init__(self, width, height, r, c):
        
        # attributes
        # geometry
        self.label_width = width
        self.label_height = height

        # grid style

        # grid positioning
        self.row = r
        self.column = c

        # label style properties
        self.label_colour = '#ffffff'

        # instantiate a Label using ctk label super class
        super().__init__(grid, width = self.label_width, height = self.label_height, text = '')
        # place in grid format
        super().grid(row = self.row, column = self.column)


# template to create all labels for a corresponding set
class Labels():
    def __init__(self, set_solution):

        # attributes
        #
        self.row_reference = convert_to_labels(set_solution)
        self.column_reference = convert_to_labels(list(zip(*set_solution)))
        #
        self.scale = len(set_solution[0])
        #
        self.place_labels()

    # create a range of labels to go beside each row and column
    def place_labels(self):
        for r in range(self.scale):
            label = Label(60, 60, r, self.scale)
            label.configure(text = format_labels(self.row_reference[r], '   '))
        for c in range(self.scale):
            label = Label(60, 60, self.scale, c)
            label.configure(text = format_labels(self.column_reference[c], '\n'))


# a function to take a Set in bitmap form to convert into labels
def convert_to_labels(set_data):
    scale = len(set_data[0])
    contents = []
    #
    for r in range(scale):
        row = []
        count = 0
        for c in range(scale):
            count += set_data[r][c]
            if (set_data[r][c] != 1 or c == scale - 1) and count > 0:
                row.append(count)
                count = 0
        contents.append(row)
    return contents


# a function to enable vertical stacking in a label
def format_labels(n_list, separator):
    # convert the list integers to strings
    s_list = [str(n) for n in n_list]
    # output a formatted string using variable separator
    return separator.join(s_list)

'''
#
def convert_to_bitmap(set_object):
    print()
'''

window = Window(600, 600)
grid = Grid(window, 540, 540, 2, 85, 85, '#212121')

# solutions

solution1 = [[0, 1, 0, 1],
             [1, 1, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 0]]

set1 = Set(4)
labels = Labels(solution1)


# event loop
window.mainloop()