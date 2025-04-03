from customtkinter import CTkButton, CTkFrame, CTkLabel


class ProfileCreationView(CTkFrame):
    def __init__(self, root, **kwargs):
        super().__init__(root)

        self.root = root
        self.window_bg = root.cget('fg_color')
        self.configure(fg_color=self.window_bg)

        message = CTkLabel(
            self,
            text='Profile Creation',
            font=('Segoe UI', 36)
        )
        message.grid(row=0, column=0, columnspan=2, padx=0, pady=(30, 0))

        backbutton = CTkButton(
            self,
            width=100,
            height=30,
            text="Back",
            command=self.go_to_previous_page
        )
        backbutton.grid(row=1, column=0, padx=5, pady=5)

    def go_to_previous_page(self):
        from gui import FrameManager, Frames
        FrameManager.load_frame(self.root, Frames.PROFILE_SELECTION)

