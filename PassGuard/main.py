from gui import Window, FrameManager, Frames

def create_main_window() -> Window:
    window_width = 800
    window_height = 600
    window_title = "PassGuard"
    resize_window = False
    return Window(window_width, window_height, window_title, resize_window)


def main() -> None:
    app = create_main_window()
    FrameManager.load_frame(app, Frames.PROFILE_SELECTION)
    app.mainloop()


if __name__ == '__main__':
    main()
