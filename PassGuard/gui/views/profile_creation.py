from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkImage, filedialog
from utils.hashing_handler import HashingHandler
from gui.components import Toast
from controllers import ProfileController
from utils.runtime import get_asset_directory, get_profile_directory
from PIL import Image, ImageEnhance


class ProfileCreationView(CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root)
        self.root = root
        self.window_bg = root.cget('fg_color')
        self.configure(fg_color=self.window_bg)
        self.profile_image, self.profile_image_path = self.set_default_image()
        self.display_view_components()


    def set_default_image(self):
        default_image_path = get_asset_directory() + "default_avatar.png"
        default_image = Image.open(default_image_path)
        return default_image, default_image_path

    def display_view_components(self):
        message = CTkLabel(
            self,
            text='Profile Creation',
            font=('Segoe UI', 36)
        )
        message.grid(row=0, column=0, columnspan=2, padx=0, pady=(30, 0))

        self.display_profile_image_button()

        profile_name_label = CTkLabel(
            self,
            width=250,
            text="Profile Name:",
            font=("Segoe UI", 16),
            anchor="w"
        )
        profile_name_label.grid(row=3, column=0, columnspan=2, padx=0, pady=0)

        self.profile_name_entry = CTkEntry(
            self,
            width=250,
            height=30
        )
        self.profile_name_entry.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        root_password_label = CTkLabel(
            self,
            width=250,
            text="Password: ",
            font=("Segoe UI", 16),
            anchor="w"
        )
        root_password_label.grid(row=5, column=0, columnspan=2, padx=0, pady=0)

        self.root_password_entry = CTkEntry(
            self,
            width=250,
            height=30,
            show="*"
        )
        self.root_password_entry.grid(row=6, column=0, columnspan=2, padx=0, pady=0)

        confirm_password_label = CTkLabel(
            self,
            width=250,
            text="Confirm Password: ",
            font=("Segoe UI", 16),
            anchor="w"
        )
        confirm_password_label.grid(row=7, column=0, columnspan=2, padx=0, pady=0)

        self.confirm_password_entry = CTkEntry(
            self,
            width=250,
            height=30,
            show="*"
        )
        self.confirm_password_entry.grid(row=8, column=0, columnspan=2, padx=0, pady=0)

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
        default_profile_image = CTkImage(self.profile_image, size=(100, 100))
        profile_image_button = CTkButton(
            self,
            width=90,
            height=90,
            text ="",
            fg_color="transparent",
            hover_color=self.window_bg,
            image=default_profile_image,
            cursor="hand2",
            command=lambda: self.load_custom_profile_image(profile_image_button)
        )
        profile_image_button.grid(row=2, column=0, columnspan=2, padx=0, pady=10)
        profile_image_button.bind("<Enter>", lambda event, b=profile_image_button: self.profile_image_hover(event, b))
        profile_image_button.bind("<Leave>", lambda event, b=profile_image_button: self.profile_image_leave(event, b))


    def load_custom_profile_image(self, profile_image_button):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        new_profile_image = Image.open(image_path)
        self.profile_image = new_profile_image
        self.profile_image_path = image_path
        new_image = CTkImage(new_profile_image, size=(100, 100))
        profile_image_button.configure(image=new_image)

    def profile_image_hover(self, event, profile_image_button):
        darker_image = ImageEnhance.Brightness(self.profile_image).enhance(0.5)
        hover_image = CTkImage(darker_image, size=(100, 100))
        profile_image_button.configure(image=hover_image)

    def profile_image_leave(self, event, profile_image_button):
        default_image = CTkImage(self.profile_image, size=(100, 100))
        profile_image_button.configure(image=default_image)

    def check_for_empty_inputs(self):
        TOAST_DELAY = 3000
        if len(self.profile_name_entry.get()) == 0:
            Toast(self.root, "Name cannot be empty", TOAST_DELAY)
            return True
        elif len(self.root_password_entry.get()) == 0:
            Toast(self.root, "Root password cannot be empty", TOAST_DELAY)
            return True
        elif len(self.confirm_password_entry.get()) == 0:
            Toast(self.root, "Confirm password cannot be empty", TOAST_DELAY)
            return True
        return False


    def create_profile(self):
        from gui import FrameManager, Frames
        is_inputs_empty = self.check_for_empty_inputs()
        if not is_inputs_empty:
            if self.root_password_entry.get() == self.confirm_password_entry.get():
                hashed_password = HashingHandler.hash(self.root_password_entry.get())
                profile_directory = get_profile_directory()
                profile_file_name = self.profile_name_entry.get().replace(" ", "_")
                file_content = f"{self.profile_image_path}\n{self.profile_name_entry.get()}\n{hashed_password}"
                ProfileController.create_profile(profile_directory, profile_file_name, file_content)
                FrameManager.load_frame(self.root, Frames.PROFILE_SELECTION)
            else:
                Toast(self.root, "Passwords don't match", 3000)

    def go_to_previous_page(self):
        from gui import FrameManager, Frames
        FrameManager.load_frame(self.root, Frames.PROFILE_SELECTION)

