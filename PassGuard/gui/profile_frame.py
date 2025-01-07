from customtkinter import CTkFrame, CTkLabel, CTkButton, get_appearance_mode

class ProfilePage(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.window = master
        window_bg = master.cget('fg_color')
        self.configure(fg_color=window_bg)

        welcome_message = CTkLabel(
            self,
            text='Welcome',
            font=('Segoe UI', 36)
        )
        welcome_message.grid(row=0, column=0, padx=20, pady=(30, 0))

        profile_message = CTkLabel(
            self,
            text='Please select a profile to continue',
            font=('Segoe UI', 16)
        )
        profile_message.grid(row=1, column=0, padx=0, pady=3)

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

        if get_appearance_mode() == "Dark":
            self.create_new_profile_button.configure(fg_color="gray10")

        self.create_new_profile_button.grid(row=2, column=0, padx=0, pady=30)

    def create_new_profile(self):
        from controllers import PageController, Pages
        PageController.set_page(self.window, Pages.CREATE_PROFILE)

    def on_hover(self, event):
        if get_appearance_mode() == "Dark":
            self.create_new_profile_button.configure(
                text_color='white',
                fg_color='#141414'
            )
        else:
            self.create_new_profile_button.configure(
                text_color='white',
                fg_color='gray'
            )

    def on_leave(self, event):
        if get_appearance_mode() == "Dark":
            self.create_new_profile_button.configure(
                text_color='white',
                fg_color='gray10'
            )
        else:
            self.create_new_profile_button.configure(
                text_color='white',
                fg_color='lightgray'
            )
