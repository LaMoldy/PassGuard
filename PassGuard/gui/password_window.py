from customtkinter import CTkEntry, CTkLabel, CTkToplevel, CTkButton


class PasswordWindow(CTkToplevel):
    RESIZABLE = False
    WIDTH=400
    HEIGHT=200

    password = ""

    def __init__(self, master, profile_directory, profile_name, callback, **kwargs):
        super().__init__(master, **kwargs)

        self.title(f"Verification: {profile_name}")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(self.RESIZABLE, self.RESIZABLE)
        self.callback = callback
        self.profile_directory = profile_directory

        self.profile_name = profile_name
        label = "Please enter root password for " + profile_name
        password_label = CTkLabel(
            self,
            text=label,
            font=("Segoe UI", 16)
        )
        password_label.pack(padx=00, pady=20)

        self.password_entry = CTkEntry(
            self,
            width=200,
            height=35,
            show="*"
        )
        self.password_entry.pack(padx=0, pady=5)

        submit_button = CTkButton(
            self,
            width=100,
            height=35,
            text="Submit",
            command=self.submit_password
        )
        submit_button.pack(padx=0, pady=10)

        self.transient(master)
        self.grab_set()
        master.wait_window(self)

    def get_profile_password(self):
        from controllers import Profile
        password = Profile.get_profile_password(self.profile_directory, self.profile_name)
        return password

    def compare_passwords(self, hashed_password):
        from controllers import Password
        return Password.compare(hashed_password, Password.hash(self.password_entry.get()))

    def submit_password(self):
        from gui.widgets import  Toast
        hashed_password = self.get_profile_password()
        if self.compare_passwords(hashed_password):
            self.callback(True)
            self.destroy()
        Toast(self, "Passwords did not match", 3000)
        self.password_entry.delete(0,len(self.password_entry.get()))
