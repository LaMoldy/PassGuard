from customtkinter import CTk, CTkFrame
from enum import Enum
from gui import ProfilePage

class Pages(Enum):
    PROFILE = 0
    
class PageController():
    previous_page = None

    @classmethod
    def set_page(self, root: CTk, next_page: Pages):
        if self.previous_page:
            self.previous_page.pack_forget()
        page = self._get_page(root, next_page)
        page.pack(pady=150)
        self.previous_page = page

    @staticmethod
    def _get_page(root: CTk, page: Pages) -> CTkFrame:
        match (page):
            case Pages.PROFILE:
                return ProfilePage(root)
            case _:
                return ProfilePage(root)
