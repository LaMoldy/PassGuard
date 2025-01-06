from customtkinter import CTkFrame, CTkLabel

class CreateProfilePage(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.message = CTkLabel(
            self,
            text="Create Profile"
        )
        self.message.pack(padx=0, pady=0)
