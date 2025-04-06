import pytest
import os
import sys
from PIL import Image
from customtkinter import CTk
from gui.frame_manager import FrameManager, Frames
from gui.views import ProfileSelectionView
from utils.runtime import get_asset_directory
from unittest.mock import patch

class TestFrameManager:
    @pytest.fixture(scope="class", autouse=True)
    def setup_headless(self, tmp_path_factory):
        # Set environment variables for headless mode
        os.environ['DISPLAY'] = ':0'
        
        # Set Tcl/Tk environment variables for Windows
        if sys.platform.startswith('win'):
            import tkinter
            root = tkinter.Tk()
            
            # Get Tcl/Tk paths directly from the running interpreter
            tcl_lib = root.tk.exprstring('$tcl_library')
            tk_lib = root.tk.exprstring('$tk_library')
            
            # Clean up the temporary root window
            root.destroy()
            
            print(f"Found Tcl/Tk libraries at: {tcl_lib} and {tk_lib}")
            
            # Set environment variables
            os.environ['TCL_LIBRARY'] = tcl_lib
            os.environ['TK_LIBRARY'] = tk_lib
        else:
            # For Unix-like systems
            os.environ['DISPLAY'] = ':0'

        # Create asset directory and default avatar
        asset_dir = tmp_path_factory.mktemp("assets")
        default_image = Image.new('RGB', (100, 100), color='blue')
        default_image_path = asset_dir / "default_avatar.png"
        default_image.save(default_image_path)

        # Mock get_asset_directory to return our temporary asset directory
        with patch('utils.runtime.get_asset_directory', return_value=str(asset_dir)):
            yield
        
        # Clean up
        if 'DISPLAY' in os.environ:
            del os.environ['DISPLAY']
        if 'TCL_LIBRARY' in os.environ:
            del os.environ['TCL_LIBRARY']
        if 'TK_LIBRARY' in os.environ:
            del os.environ['TK_LIBRARY']
        if 'TCL_DEFAULT_LIBRARY' in os.environ:
            del os.environ['TCL_DEFAULT_LIBRARY']
        if 'TK_DEFAULT_LIBRARY' in os.environ:
            del os.environ['TK_DEFAULT_LIBRARY']

    @pytest.fixture(scope="class")
    def root(self):
        root = CTk()
        yield root
        root.destroy()

    def test_get_frame_profile_selection(self, root):
        frame = FrameManager.get_frame(root, Frames.PROFILE_SELECTION)
        assert isinstance(frame, ProfileSelectionView)
        assert frame.master == root

    def test_load_frame_initial_load(self, root):
        FrameManager.load_frame(root, Frames.PROFILE_SELECTION)
        assert FrameManager.previous_frame is not None
        assert isinstance(FrameManager.previous_frame, ProfileSelectionView)

    def test_load_frame_switch_frames(self, root):
        # Load first frame
        FrameManager.load_frame(root, Frames.PROFILE_SELECTION)
        first_frame = FrameManager.previous_frame
        
        # Load second frame (same type for now since we only have one frame type)
        FrameManager.load_frame(root, Frames.PROFILE_SELECTION)
        second_frame = FrameManager.previous_frame
        
        # Verify frames are different instances
        assert first_frame != second_frame
        # Verify previous frame was properly updated
        assert FrameManager.previous_frame == second_frame

    def test_load_frame_forgets_previous(self, root):
        # Load first frame
        FrameManager.load_frame(root, Frames.PROFILE_SELECTION)
        first_frame = FrameManager.previous_frame
        
        # Load second frame
        FrameManager.load_frame(root, Frames.PROFILE_SELECTION)
        
        # Verify first frame is no longer visible
        assert not first_frame.winfo_viewable()
