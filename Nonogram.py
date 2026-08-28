
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

        # state
        self.is_flipped = 0

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
        if self.is_flipped == 0:
            self.is_flipped = 1
        else:
            self.is_flipped = 0
        self.configure(fg_color = set_box_colour, hover_color = set_hover_colour)


# template to create a grid of Boxes
class Set():
    def __init__(self, scale, solution):
        
        # attributes
        # define a set
        self.set_list = []
        self.solution = solution
        
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

    # returns a list of set objects and solution
    def output_set_info(self):
        return {'List': self.set_list, 'Solution': self.solution}


#
class Submit(ctk.CTkButton):
    def __init__(self, parent, text, display_set):

        # attributes
        # parent widget
        self.container = parent

        self.display_set = display_set

        # geometry
        self.button_width = 60
        self.button_height = 60
        self.c_radius = 0

        # style properties
        self.button_colour = '#212121'
        self.hover = '#282828'

        # text
        self.text_contents = text
        
        # instantiate a ctk button using the super class
        super().__init__(window, width = self.button_width, height = self.button_height, 
        text = self.text_contents, corner_radius = self.c_radius, fg_color = self.button_colour, 
        hover_color = self.hover, command = self.set_check)
        # place using fixed coordinates
        super().place(x = 425, y = 85)        

    # 
    def set_check(self):
        if convert_to_bitmap(self.display_set) == self.display_set.output_set_info()['Solution']:
            print('+')
        else:
            print('-')


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


# a function to convert a set object to a matrix of bits
def convert_to_bitmap(set_object):
    bits = []
    for box_list in set_object.set_list:
        local_bits = []
        for box in box_list:
            local_bits.append(box.is_flipped)
        bits.append(local_bits)
    return bits


window = Window(600, 600)
grid = Grid(window, 540, 540, 2, 85, 85, '#212121')

# solutions

# 3 x 3

solution1 = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]

# 4 x 4

solution2 = [[0, 1, 0, 1],
             [1, 1, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 0]]

set1 = Set(3, solution1)
labels = Labels(solution1)

submit_button = Submit(window, '', set1)

# event loop
window.mainloop()