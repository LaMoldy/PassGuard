from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, get_appearance_mode
from controllers import ProfileController

class ProfileSelectionView(CTkFrame):
    def __init__(self, root: CTk, **kwargs):
        super().__init__(root, **kwargs)

        window_bg = root.cget('fg_color')
        self.configure(fg_color=window_bg)

        self.display_view_components()


    def display_view_components(self):
        profile_names = ProfileController.get_profile_names("profiles/")
        profiles_button_count = len(profile_names) + 1 if len(profile_names) < 5 else 5

        view_title = "Profile Selection"
        view_title_label = CTkLabel(
            self,
            text=view_title,
            font=("Segoe UI", 36)
        )
        view_title_label.grid(row=0, column=0, columnspan=profiles_button_count, padx=0, pady=(25, 0))
        self.display_profile_buttons(profile_names)

    def display_too_many_profile_message(self):
        error_message = "There are too many profiles located in: "
        error_message_label = CTkLabel(
            self,
            text=error_message,
            font=("Segoe UI", 16)
        )
        error_message_label.grid(row=3, column=0, padx=0, pady=(25,0))

        remove_file_message = "Please remove the profile files until you only have five remaining and restart the app"
        remove_file_message_label = CTkLabel(
            self,
            text=remove_file_message,
            font=("Segoe UI", 16)
        )
        remove_file_message_label.grid(row=4, column=0, padx=0, pady=0)


    def display_profile_buttons(self, profile_names):
        if len(profile_names) >= 0 :
            profile_count = 0
            for profile in profile_names:
                profile_button = CTkButton(
                    self,
                    width=90,
                    height=90,
                    corner_radius=8,
                    cursor="hand2",
                    text="",
                    compound="top"
                )
                profile_button.grid(row=2, column=profile_count, padx=3, pady=(25, 0))
                profile_count = profile_count + 1
            if profile_count < 5:
                self.display_new_profile_button(profile_count)
        else:
            self.display_too_many_profile_message()


    def display_new_profile_button(self, previous_profiles: int):
        self.create_new_profile_button = CTkButton(
            self,
            width=100,
            height=100,
            corner_radius=0,
            text="+",
            text_color="gray",
            font=("Arial", 40),
            fg_color="lightgrey",
            cursor="hand2",
            command=self.create_new_profile
        )

        if get_appearance_mode() == "Dark":
            self.create_new_profile_button.configure(fg_color="gray10")

        self.create_new_profile_button.grid(row=2, column=previous_profiles, columnspan=(previous_profiles + 1), padx=3, pady=(25, 0))
        self.create_new_profile_button.bind("<Enter>", self.create_profile_on_hover)
        self.create_new_profile_button.bind("<Leave>", self.create_profile_on_leave)

    def create_new_profile(self):
        print("Create new profile")

    def create_profile_on_hover(self, event):
        if get_appearance_mode() == "Dark":
            self.create_new_profile_button.configure(fg_color="#141414", text_color="white")
        else:
            self.create_new_profile_button.configure(fg_color="gray", text_color="white")

    def create_profile_on_leave(self, event):
        if get_appearance_mode() == "Dark":
            self.create_new_profile_button.configure(fg_color="gray10", text_color="white")
        else:
            self.create_new_profile_button.configure(fg_color="lightgrey", text_color="white")
