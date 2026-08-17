
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


window = Window(600, 600)

# event loop
window.mainloop()