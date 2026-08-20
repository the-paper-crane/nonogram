
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
        self.set_icon(tk.PhotoImage(file = "/home/crane/Pictures/2026-08-19_08-58.png"))
        self.title("Nonogram")

    def set_icon(self, icon_path):
        self.wm_iconphoto(False, icon_path)

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

# event loop
window.mainloop()