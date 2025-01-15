from customtkinter import CTkFrame, CTkLabel

class PasswordHubPage(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        message = CTkLabel(
            self,
            text="Welcome to the password hub"
        )
        message.grid(row=0, column=0, columnspan=2, padx=0, pady=0)
