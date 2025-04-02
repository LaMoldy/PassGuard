import os
import platform
import sys

from tkinter import PhotoImage
from customtkinter import CTk, set_appearance_mode
from utils import is_exe

class Window(CTk):
    def __init__(self, width: int, height: int,
                 title: str, win_resizable: bool, default_theme: str = "dark") -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(win_resizable, win_resizable)
        self.set_window_icon()
        set_appearance_mode(default_theme)

    def get_icon_paths(self) -> tuple[str, str]:
        window_icon = ""
        window_image = ""
        if is_exe():
            window_icon = os.path.join(sys._MEIPASS, "assets/logo.ico") # type: ignore
            window_image = os.path.join(sys._MEIPASS, "assets/logo.png") # type: ignore
        else:
            window_icon = "assets/logo.ico"
            window_image = "assets/logo.png"
        return window_icon, window_image

    def set_window_icon(self):
        window_icon, window_image = self.get_icon_paths()
        if platform.system() == "Windows":
            self.iconbitmap(window_icon)
        else:
            icon_image = PhotoImage(file=window_image)
            self.iconphoto(True, icon_image)


