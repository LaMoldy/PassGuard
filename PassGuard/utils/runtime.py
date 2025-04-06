from os import path
import sys

def is_exe() -> bool:
    """
    Checks if the application is running as a PyInstaller executable

    Returns:
        bool: True if running as an executable, False otherwise
    """
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

def get_profile_directory() -> str:
    """
    Gets the directory of the project

    Returns:
        str: The directory of the project
    """
    if is_exe():
        return path.join(sys._MEIPASS, "profiles")# type: ignore
    return "profiles/"
