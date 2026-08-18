
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
        self.set_icon(tk.PhotoImage(file = "/home/legolas/Downloads/GoogleIcons/CubeIcon.png"))
        self.title("Nonogram")

        def set_icon(self, icon_path):
            self.wm_iconphoto(False, icon_path)


window = Window(600, 600)

# event loop
window.mainloop()