import customtkinter
import platform
from PIL import ImageTk

class App(customtkinter.CTk):
    TITLE = 'PassGuard'
    WIDTH = 800
    HEIGHT = 500
    WIDTH_RESIZABLE = False
    HEIGHT_RESIZABLE = False
    WINDOW_ICON = './assets/logo.ico'
    WINDOW_IMAGE = './assets/logo.png'
    DEFAULT_APPEARANCE = 'light'

    def __init__(self):
        super().__init__()
        self.title(self.TITLE)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(self.WIDTH_RESIZABLE, self.HEIGHT_RESIZABLE)

        # Setting the window icon
        if platform.system() == 'Windows':
            self.iconbitmap(self.WINDOW_ICON) # This is only supported on Windows
        else:
            self.iconimage = ImageTk.PhotoImage(file=self.WINDOW_IMAGE)
            self.iconphoto(True, self.iconimage)

        customtkinter.set_appearance_mode(self.DEFAULT_APPEARANCE)
