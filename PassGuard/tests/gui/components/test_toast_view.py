import pytest
import os
from customtkinter import CTk
from gui.components.toast import Toast

class TestToast:
    @pytest.fixture(scope="class", autouse=True)
    def setup_headless(self):
        # Set environment variable to use headless mode
        os.environ['DISPLAY'] = ':0'
        yield
        # Clean up
        if 'DISPLAY' in os.environ:
            del os.environ['DISPLAY']

    @pytest.fixture(scope="class")
    def root(self):
        root = CTk()
        yield root
        root.destroy()

    def test_initialization(self, root):
        message = "Test message"
        duration = 2000
        toast = Toast(root, message, duration)
        
        assert isinstance(toast, Toast)
        assert toast.parent == root
        assert toast.message == message
        assert toast.duration == duration
        assert toast.overrideredirect()
        assert toast.cget("fg_color") == "#FF6666"

    def test_setup_ui(self, root):
        toast = Toast(root, "Test message")
        
        # Verify window size
        assert toast.winfo_width() == 240
        assert toast.winfo_height() == 50
        
        # Verify label properties
        label = toast.label
        assert label.cget("text") == "Test message"
        assert label.cget("text_color") == "white"
        assert label.cget("font") == ("Segoe UI", 14)

    def test_update_position(self, root):
        toast = Toast(root, "Test message")
        
        # Set parent window position and size
        root.geometry("800x600+100+200")
        root.update()
        
        # Call update_position
        toast.update_position()
        
        # Get the current position
        x = toast.winfo_x()
        y = toast.winfo_y()
        
        # Verify position is correct (relative to parent)
        assert x == 100 + 800 - 240 - 10  # parent_x + parent_width - win_width - 10
        assert y == 200 + 50  # parent_y + 50

    def test_on_parent_move(self, root):
        toast = Toast(root, "Test message")
        
        # Store initial position
        initial_x = toast.winfo_x()
        initial_y = toast.winfo_y()
        
        # Move parent window
        root.geometry("+150+250")
        root.update()
        
        # Trigger parent move event
        toast.on_parent_move()
        
        # Get new position
        new_x = toast.winfo_x()
        new_y = toast.winfo_y()
        
        # Verify position changed
        assert new_x != initial_x
        assert new_y != initial_y

    def test_destroy_toast(self, root):
        toast = Toast(root, "Test message")
        
        # Store the bind_id before destruction
        bind_id = toast.bind_id
        
        # Call destroy_toast
        toast.destroy_toast()
        
        # Verify window is destroyed
        assert not toast.winfo_exists()