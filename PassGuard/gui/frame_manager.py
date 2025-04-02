from customtkinter import CTk, CTkFrame
from enum import Enum
from gui.views import ProfileSelectionView

class Frames(Enum):
    PROFILE_SELECTION = 0

class FrameManager:
    previous_frame = None

    @classmethod
    def load_frame(cls, root: CTk, next_frame: Frames) -> None:
        if cls.previous_frame:
            cls.previous_frame.pack_forget()
        frame = FrameManager.get_frame(root, next_frame)
        frame.pack(pady=20)
        cls.previous_frame = frame

    @staticmethod
    def get_frame(root: CTk, frame: Frames) -> CTkFrame:
        match frame:
            case Frames.PROFILE_SELECTION:
                return ProfileSelectionView(root)
