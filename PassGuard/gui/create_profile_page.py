from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, filedialog
from PIL import Image, ImageEnhance
from gui.widgets import Toast
import sys
import os

class CreateProfilePage(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.window = master
        self.profile_image = None
        self.current_dir = None

        ENTRY_WIDTH = 250
        ENTRY_HEIGHT = 30
        ENTRY_LABEL_FONT = ('Segoe UI', 16)

        window_bg = master.cget('fg_color')
        self.configure(fg_color=window_bg)

        message = CTkLabel(
            self,
            text='Profile Creation',
            font=('Segoe UI', 36)
        )
        message.grid(row=0, column=0, columnspan=2, padx=0, pady=(30, 0))

        if getattr(sys, 'frozen', False):  # This is used for exe version
            exe_path = sys.executable
            self.current_dir = os.path.dirname(exe_path)
            self.image_path = os.path.join(self.current_dir, 'assets/default_avatar.png')
        else:
            self.image_path = 'assets/default_avatar.png' # This is used for running with python in cmd

        self.default_image = Image.open(self.image_path)
        self.profile_image = self.default_image
        default_button_image = CTkImage(self.default_image, size=(100, 100))
        self.profile_image_button = CTkButton(
            self,
            width=90,
            height=90,
            text='',
            image=default_button_image,
            fg_color='transparent',
            hover_color=window_bg,
            cursor='hand2',
            command=self.upload_custom_profile_picture
        )
        self.profile_image_button.bind('<Enter>', self.on_hover)
        self.profile_image_button.bind('<Leave>', self.on_hover_leave)
        self.profile_image_button.grid(row=2, column=0, columnspan=2, padx=0, pady=10)

        profile_name_label = CTkLabel(
            self,
            width=250,
            text='Name:',
            font=ENTRY_LABEL_FONT,
            anchor='w'
        )
        profile_name_label.grid(row=3, column=0, columnspan=2, padx=0, pady=0)

        self.profile_name_entry = CTkEntry(
            self,
            width=ENTRY_WIDTH,
            height=ENTRY_HEIGHT
        )
        self.profile_name_entry.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        root_password_label = CTkLabel(
            self,
            width=250,
            text='Root Password:',
            font=ENTRY_LABEL_FONT,
            anchor='w'
        )
        root_password_label.grid(row=5, column=0, columnspan=2, padx=0, pady=0)

        self.root_password_entry = CTkEntry(
            self,
            width=ENTRY_WIDTH,
            height=ENTRY_HEIGHT,
            show="*"
        )
        self.root_password_entry.grid(row=6, column=0, columnspan=2, padx=0, pady=0)

        confirm_password_label = CTkLabel(
            self,
            width=250,
            text='Confirm Password:',
            font=('Segoe UI', 16),
            anchor='w'
        )
        confirm_password_label.grid(row=7, column=0, columnspan=2, padx=0, pady=0)

        self.confirm_password_entry = CTkEntry(
            self,
            width=ENTRY_WIDTH,
            height=ENTRY_HEIGHT,
            show="*"
        )
        self.confirm_password_entry.grid(row=8, column=0, columnspan=2, padx=0, pady=0)

        self.back_button = CTkButton(
            self,
            width=100,
            height=30,
            text='Back',
            command=self.go_to_previous_page,
        )
        self.back_button.grid(row=9, column=0, padx=(0, 20), pady=30)

        self.create_profile_button = CTkButton(
            self,
            width=100,
            height=30,
            text='Create',
            command=self.create_profile,
        )
        self.create_profile_button.grid(row=9, column=1, padx=(20, 0), pady=30)

    def on_hover(self, event):
        darker_button_image = ImageEnhance.Brightness(self.profile_image).enhance(0.5)
        hover_image = CTkImage(darker_button_image, size=(100, 100))
        self.profile_image_button.configure(image=hover_image)

    def on_hover_leave(self, event):
        default_image = CTkImage(self.profile_image, size=(100, 100))
        self.profile_image_button.configure(image=default_image)

    def upload_custom_profile_picture(self):
        self.image_path = filedialog.askopenfilename()
        new_profile_image = Image.open(self.image_path)
        self.profile_image = new_profile_image
        profile_image = CTkImage(new_profile_image, size=(100, 100))
        self.profile_image_button.configure(image=profile_image)

    def go_to_previous_page(self):
        from controllers import PageController, Pages
        PageController.set_page(self.window, Pages.PROFILE)

    def check_for_empty_inputs(self) -> bool:
        TOAST_DELAY = 3000
        if len(self.profile_name_entry.get()) == 0:
            Toast(self.window, "Name cannot be empty", TOAST_DELAY)
            return True
        elif len(self.root_password_entry.get()) == 0:
            Toast(self.window, "Root password cannot be empty", TOAST_DELAY)
            return True
        elif len(self.confirm_password_entry.get()) == 0:
            Toast(self.window, "Confirm password cannot be empty", TOAST_DELAY)
            return True
        return False

    def create_profile(self):
        from controllers import PageController, Pages, Profile
        is_empty = self.check_for_empty_inputs()
        if not is_empty:
            if self.root_password_entry.get() == self.confirm_password_entry.get():
                file_name = f"profiles/{self.profile_name_entry.get()}.profile"
                msg, successful = Profile.create_profile(
                    file_name,
                    self.current_dir,
                    self.profile_name_entry.get(),
                    self.root_password_entry.get(),
                    self.image_path
                )
                if successful:
                    PageController.set_page(self.window, Pages.PASSWORD_HUB)
                else:
                    Toast(self.window, msg, 3000)
            else:
                Toast(self.window, "Passwords don't match", 3000)

