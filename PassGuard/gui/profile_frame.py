import customtkinter

class ProfilePage(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        welcome_message = customtkinter.CTkLabel(
            self,
            text='Welcome',
            font=("Segoe UI", 36)
        )
        welcome_message.grid(row=0, column=0, padx=20, pady=5)
