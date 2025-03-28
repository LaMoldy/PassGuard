from customtkinter import CTk, CTkFrame
from enum import Enum
from gui import ProfilePage, CreateProfilePage, PasswordHubPage

class Pages(Enum):
    PROFILE = 0
    CREATE_PROFILE = 1
    PASSWORD_HUB = 2

class PageController():
    previous_page = None

    @classmethod
    def set_page(cls, root: CTk, next_page: Pages, data=""):
        if cls.previous_page:
            cls.previous_page.pack_forget()
        page = PageController._get_page(root, next_page)
        page.pack(pady=20)
        cls.previous_page = page

    @staticmethod
    def _get_page(root: CTk, page: Pages, data="") -> CTkFrame:
        match (page):
            case Pages.PROFILE:
                return ProfilePage(root)
            case Pages.CREATE_PROFILE:
                return CreateProfilePage(root)
            case Pages.PASSWORD_HUB:
                return PasswordHubPage(root, data)
