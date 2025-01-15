from customtkinter import CTk, set_appearance_mode
import platform
import os
import sys
from PIL import ImageTk

class App(CTk):
    TITLE = 'PassGuard'
    WIDTH = 800
    HEIGHT = 500
    WIDTH_RESIZABLE = False
    HEIGHT_RESIZABLE = False
    DEFAULT_APPEARANCE = 'dark'

    exe_path = ''
    current_dir = ''
    window_icon = ''
    window_image = ''

    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
        current_dir = os.path.dirname(exe_path)
        window_icon = os.path.join(f"{current_dir}", 'assets/logo.ico')
        window_image = os.path.join(current_dir, 'assets/logo.png')
    else:
        window_icon = 'assets/logo.ico'
        window_image = 'assets/logo.png'

    def __init__(self):
        super().__init__()
        self.title(self.TITLE)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(self.WIDTH_RESIZABLE, self.HEIGHT_RESIZABLE)

        # Setting the window icon
        if platform.system() == 'Windows':
            self.iconbitmap(self.window_icon) # This is only supported on Windows
        else:
            self.iconimage = ImageTk.PhotoImage(file=self.window_image)
            self.iconphoto(True, self.iconimage)

        set_appearance_mode(self.DEFAULT_APPEARANCE)
