import sys

def is_exe() -> bool:
    """
    Checks if the application is running as a PyInstaller executable

    Returns:
        bool: True if running as an executable, False otherwise
    """
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

