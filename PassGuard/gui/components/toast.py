from customtkinter import CTkToplevel, CTkLabel

class Toast(CTkToplevel):
    def __init__(self, parent, message, duration):
        super().__init__(parent)
        self.geometry("240x50")
        self.overrideredirect(True)
        self.configure(fg_color="FF6666", corner_radius=20)
        self.parent = parent
        self.message = message
        self.duration = duration
        self.bind_id = self.parent.bind("<Configure>", self.on_parent_move)

    def display_toast_components(self):
        label = CTkLabel(
            self,
            text=self.message,
            text_color="white",
            font=("Segoe UI", 14)
        )
        label.pack(expand=True, fill="both", padx=10, pady=10)

    def update_position(self):
        parent_x = self.parent.winfo_x()
        parent_y = self.parent.winfo_y()
        parent_width = self.parent.winfo_width()
        x = parent_x + parent_width - self.winfo_width() - 10
        y = parent_y + 50
        self.geometry(f"+{x}+{y}")

    def on_parent_move(self, event):
       self.update_position()

    def destroy_toast(self):
        self.parent.unbind("<Configure>", self.bind_id)
        self.destroy()

    def show_toast(self):
        self.after(self.duration, self.destroy_toast)
