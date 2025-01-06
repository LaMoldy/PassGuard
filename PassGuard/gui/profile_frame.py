from customtkinter import CTkFrame, CTkLabel, CTkButton

class ProfilePage(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.window = master
        window_bg = master.cget('fg_color')
        self.configure(fg_color=window_bg)

        self.welcome_message = CTkLabel(
            self,
            text='Welcome',
            font=('Segoe UI', 36)
        )
        self.welcome_message.grid(row=0, column=0, padx=20, pady=(30, 0))

        self.profile_message = CTkLabel(
            self,
            text='Please select a profile to continue',
            font=('Segoe UI', 16)
        )
        self.profile_message.grid(row=1, column=0, padx=0, pady=3)

        self.create_new_profile_button = CTkButton(
            self,
            width=100,
            height=100,
            corner_radius=3,
            text = '+',
            text_color='gray',
            font=('Arial', 40),
            fg_color='lightgray',
            anchor='center',
            cursor='hand2',
            command=self.create_new_profile
        )
        self.create_new_profile_button.bind('<Enter>', self.on_hover)
        self.create_new_profile_button.bind('<Leave>', self.on_leave)
        self.create_new_profile_button.grid(row=2, column=0, padx=0, pady=30)

    def create_new_profile(self):
        from controllers import PageController, Pages
        PageController.set_page(self.window, Pages.CREATE_PROFILE)

    def on_hover(self, event):
        self.create_new_profile_button.configure(
            text_color='white',
            fg_color='gray'
        )

    def on_leave(self, event):
        self.create_new_profile_button.configure(
            text_color='gray',
            fg_color='lightgray'
        )
