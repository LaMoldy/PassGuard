from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkEntry


class ProfileCreationView(CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root)

        self.root = root
        self.window_bg = root.cget('fg_color')
        self.configure(fg_color=self.window_bg)

        self.display_view_components()


    def display_view_components(self):
        message = CTkLabel(
            self,
            text='Profile Creation',
            font=('Segoe UI', 36)
        )
        message.grid(row=0, column=0, columnspan=2, padx=0, pady=(30, 0))

        # Image
        self.display_profile_image_button()

        profile_name_label = CTkLabel(
            self,
            width=250,
            text="Profile Name:",
            font=("Segoe UI", 16),
            anchor="w"
        )
        profile_name_label.grid(row=3, column=0, columnspan=2, padx=0, pady=0)

        profile_name_entry = CTkEntry(
            self,
            width=250,
            height=30
        )
        profile_name_entry.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        root_password_label = CTkLabel(
            self,
            width=250,
            text="Password: ",
            font=("Segoe UI", 16),
            anchor="w"
        )
        root_password_label.grid(row=5, column=0, columnspan=2, padx=0, pady=0)

        root_password_entry = CTkEntry(
            self,
            width=250,
            height=30,
            show="*"
        )
        root_password_entry.grid(row=6, column=0, columnspan=2, padx=0, pady=0)

        confirm_password_label = CTkLabel(
            self,
            width=250,
            text="Confirm Password: ",
            font=("Segoe UI", 16),
            anchor="w"
        )
        confirm_password_label.grid(row=7, column=0, columnspan=2, padx=0, pady=0)

        confirm_password_entry = CTkEntry(
            self,
            width=250,
            height=30,
            show="*"
        )
        confirm_password_entry.grid(row=8, column=0, columnspan=2, padx=0, pady=0)

        backbutton = CTkButton(
            self,
            width=100,
            height=30,
            text="Back",
            command=self.go_to_previous_page
        )
        backbutton.grid(row=9, column=0, padx=(0, 20), pady=30)

        create_profile_button = CTkButton(
            self,
            width=100,
            height=30,
            text="Create",
            command=self.create_profile
        )
        create_profile_button.grid(row=9, column=1, padx=(20, 0), pady=30)

    def display_profile_image_button(self):

        profile_image_button = CTkButton(
            self,
            width=90,
            height=90,
            text ="",
            fg_color="transparent",
            hover_color=self.window_bg,
            cursor="hand2",
            command=self.load_custom_profile_image
        )
        profile_image_button.grid(row=2, column=0, columnspan=2, padx=0, pady=10)
        profile_image_button.bind("<Enter>", self.profile_image_hover)
        profile_image_button.bind("<Leave>", self.profile_image_leave)


    def load_custom_profile_image(self):
        pass

    def profile_image_hover(self, event):
        pass

    def profile_image_leave(self, event):
        pass

    def create_profile(self):
        pass

    def go_to_previous_page(self):
        from gui import FrameManager, Frames
        FrameManager.load_frame(self.root, Frames.PROFILE_SELECTION)

