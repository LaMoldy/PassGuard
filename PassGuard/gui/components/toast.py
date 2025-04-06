from customtkinter import CTkToplevel, CTkLabel

class Toast(CTkToplevel):
    def __init__(self, parent, message, duration=2000):
        super().__init__(parent)
        self.parent = parent
        self.message = message
        self.duration = duration
        self.setup_ui()
        self.update_position()
        self.show_toast()

        self.bind_id = self.parent.bind("<Configure>", self.on_parent_move)

    def setup_ui(self):
        WIN_WIDTH = 240
        WIN_HEIGHT = 50

        self.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
        self.overrideredirect(True)
        self.configure(fg_color="#FF6666", corner_radius=20)
        self.label = CTkLabel(
            self,
            text=self.message,
            text_color="white",
            font=("Segoe UI", 14)
        )
        self.label.pack(expand=True, fill="both", padx=10, pady=5)

    def update_position(self):
        parent_x = self.parent.winfo_x()
        parent_y = self.parent.winfo_y()
        parent_width = self.parent.winfo_width()
        x = parent_x + parent_width - self.winfo_width() - 10
        y = parent_y + 50
        self.geometry(f"+{x}+{y}")

    def on_parent_move(self, event=None):
        self.update_position()

    def destroy_toast(self):
        self.parent.unbind("<Configure>", self.bind_id)
        self.destroy()

    def show_toast(self):
        self.after(self.duration, self.destroy_toast)
