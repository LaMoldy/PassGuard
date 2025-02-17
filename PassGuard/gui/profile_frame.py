from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage, get_appearance_mode
from PIL import Image, ImageEnhance
import os
import sys

class ProfilePage(CTkFrame):
    def __init__(self, master, **kwargs):
        from controllers import File

        super().__init__(master, **kwargs)

        self.window = master
        self.window_bg = master.cget('fg_color')
        self.configure(fg_color=self.window_bg)
        self.profile_count = 0
        self.visibility_triggered = False
        self.profile_buttons = []

        self.window.bind("<Visibility>", self.check_profiles_and_render_page)

        welcome_message = CTkLabel(
            self,
            text='Welcome',
            font=('Segoe UI', 36)
        )
        welcome_message.grid(row=0, column=0, columnspan=5, padx=20, pady=(30, 0))

        if getattr(sys, 'frozen', False):  # This is used for exe version
            exe_path = sys.executable
            self.current_dir = os.path.dirname(exe_path)
            self.profile_path = os.path.join(self.current_dir, 'profiles')
        else:
            self.profile_path = 'profiles/'


    def display_profile_error(self):
        error_msg = 'There were too many profile files located in ' + self.profile_path
        error_message = CTkLabel(
            self,
            text=error_msg,
            font=('Segoe UI', 16)
        )
        error_message.grid(row=3, column=0, padx=0, pady=(25, 0))

        remove_file_label = CTkLabel(
            self,
            text='Please remove profiles until you have five remaining.',
            font=('Segoe UI', 16)
        )
        remove_file_label.grid(row=4, column=0, padx=0, pady=0)

    def display_profiles(self):
        from controllers import Profile
        file_names = Profile.get_profile_file_names(self.profile_path)
        image_paths = Profile.get_profile_pictures(self.profile_path)
        profile_message = CTkLabel(
            self,
            text='Please select a profile to continue',
            font=('Segoe UI', 16)
        )
        profile_message.grid(row=1, column=0, columnspan=5, padx=0, pady=0)

        column_spot = 0
        for i in range(self.profile_count):
            profile_image = Image.open(image_paths[i])
            profile_picture = CTkImage(profile_image, size=(100,100))
            profile_button = CTkButton(
                self,
                width=90,
                height=90,
                corner_radius=7,
                text_color='black',
                font=('Arial', 16),
                fg_color='transparent',
                hover_color=self.window_bg,
                cursor='hand2',
                text=' ',
                compound='top',
                image=profile_picture,
                # command=lamda: self.profile_clicked(profile_name)
            )
            if get_appearance_mode() == "Dark":
                profile_button.configure(text_color='white')

            profile_button.grid(row=2, column=column_spot, padx=3, pady=(25, 0))
            profile_button.bind('<Enter>', lambda event, b=profile_button, img=profile_image, name=file_names[i]: self.on_img_hover(event, b, img, name))
            profile_button.bind('<Leave>', lambda event, b=profile_button, img=profile_image: self.on_img_hover_leave(event, b, img))
            self.profile_buttons.append(profile_button)
            column_spot = column_spot + 1

        if self.profile_count < 5:
            self.create_new_profile_button = CTkButton(
                self,
                width=100,
                height=101,
                corner_radius=0,
                text = '+',
                text_color='gray',
                font=('Arial', 40),
                fg_color='lightgray',
                cursor='hand2',
                command=self.create_new_profile
            )
            self.create_new_profile_button.bind('<Enter>', self.on_hover)
            self.create_new_profile_button.bind('<Leave>', self.on_leave)

            if get_appearance_mode() == "Dark":
                self.create_new_profile_button.configure(fg_color="gray10")

            self.create_new_profile_button.grid(row=2, column=column_spot, padx=3, pady=0)

    def check_profiles_and_render_page(self, _):
        from controllers import Profile
        self.profile_count = Profile.count_profiles(self.profile_path)
        if self.visibility_triggered:
            return
        if self.profile_count > 5:
            self.display_profile_error()
        else:
            self.display_profiles()
        self.visibility_triggered = True

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

    def on_img_hover(self, event, btn, profile_image, profile_name):
        darker_button_image = ImageEnhance.Brightness(profile_image).enhance(0.5)
        hover_image = CTkImage(darker_button_image, size=(100, 100))
        btn.configure(image=hover_image, text=profile_name, compound='center')

    def on_img_hover_leave(self, event, btn, profile_image):
        default_image = CTkImage(profile_image, size=(100, 100))
        btn.configure(image=default_image)
        btn.configure(text=' ')