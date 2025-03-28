from customtkinter import CTkFrame, CTkLabel

class PasswordHubPage(CTkFrame):
    def __init__(self, master, profile_name="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        message_str = "Welcome to the password hub " + profile_name
        message = CTkLabel(
            self,
            text=message_str
        )
        message.grid(row=0, column=0, columnspan=2, padx=0, pady=0)
