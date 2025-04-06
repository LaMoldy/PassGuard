import pytest
import os
import sys
from PIL import Image
from customtkinter import CTk, CTkLabel, CTkButton
from unittest.mock import patch, MagicMock
from gui.views.profile_selection import ProfileSelectionView
from gui import FrameManager, Frames
from utils.runtime import get_asset_directory

class TestProfileSelectionView:
    @pytest.fixture(scope="class", autouse=True)
    def setup_headless(self):
        # Set environment variables for headless mode
        os.environ['DISPLAY'] = ':0'
        
        # Set Tcl/Tk environment variables
        if sys.platform.startswith('win'):
            # For Windows, we need to set TK_LIBRARY and TCL_LIBRARY
            python_dir = os.path.dirname(sys.executable)
            tcl_dir = os.path.join(python_dir, 'tcl')
            tk_dir = os.path.join(python_dir, 'tcl', 'tk8.6')
            
            if os.path.exists(tcl_dir) and os.path.exists(tk_dir):
                os.environ['TCL_LIBRARY'] = tcl_dir
                os.environ['TK_LIBRARY'] = tk_dir
                os.environ['TCL_DEFAULT_LIBRARY'] = tcl_dir
                os.environ['TK_DEFAULT_LIBRARY'] = tk_dir
        else:
            # For Unix-like systems
            os.environ['DISPLAY'] = ':0'
        
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

    @pytest.fixture(autouse=True)
    def cleanup_test_files(self):
        yield
        # Clean up any test profile images that might have been created
        test_image_path = os.path.join(str(self.root), "test_profile.png")
        if os.path.exists(test_image_path):
            try:
                os.remove(test_image_path)
            except Exception as e:
                print(f"Warning: Could not remove test file {test_image_path}: {e}")

    def test_initialization(self, root):
        view = ProfileSelectionView(root)
        assert isinstance(view, ProfileSelectionView)
        assert view.master == root
        assert view.window_bg == root.cget('fg_color')
        assert view.cget('fg_color') == view.window_bg

    @patch('controllers.ProfileController.get_profile_names')
    def test_display_view_components_no_profiles(self, mock_get_profile_names, root):
        mock_get_profile_names.return_value = []
        view = ProfileSelectionView(root)
        
        # Verify title label
        title_label = view.winfo_children()[0]
        assert title_label.cget('text') == "Profile Selection"
        assert title_label.cget('font') == ("Segoe UI", 36)
        
        # Verify buttons
        buttons = [child for child in view.winfo_children() if isinstance(child, CTkButton)]
        assert len(buttons) == 1  # Only the Create New Profile button
        assert buttons[0].cget('text') == "+"

    @patch('controllers.ProfileController.get_profile_names')
    @patch('controllers.ProfileController.get_profile_content_by_line_number')
    def test_display_profile_buttons(self, mock_get_content, mock_get_names, root):
        # Create a test image
        test_image = Image.new('RGB', (100, 100), color='red')
        test_image_path = os.path.join(str(root), "test_profile.png")
        test_image.save(test_image_path)
        
        try:
            mock_get_names.return_value = ["Test Profile"]
            mock_get_content.return_value = test_image_path
            
            view = ProfileSelectionView(root)
            profile_button = view.winfo_children()[1]
            assert profile_button.cget('width') == 90
            assert profile_button.cget('height') == 90
            assert profile_button.cget('corner_radius') == 7
            assert profile_button.cget('text') == " "
        finally:
            # Clean up the test image
            if os.path.exists(test_image_path):
                os.remove(test_image_path)

    @patch('controllers.ProfileController.get_profile_names')
    def test_display_too_many_profiles(self, mock_get_names, root):
        mock_get_names.return_value = ["Profile1", "Profile2", "Profile3", "Profile4", "Profile5", "Profile6"]
        view = ProfileSelectionView(root)
        error_labels = [child for child in view.winfo_children() 
                       if isinstance(child, CTkLabel) and child.cget('text').lower().startswith(('there are', 'please remove'))]
        assert len(error_labels) == 2
        assert "too many profiles" in error_labels[0].cget('text').lower()
        assert "remove the profile files" in error_labels[1].cget('text').lower()

    @patch('controllers.ProfileController.get_profile_names')
    @patch('controllers.ProfileController.get_profile_content_by_line_number')
    def test_profile_button_hover(self, mock_get_content, mock_get_names, root):
        # Create a test image
        test_image = Image.new('RGB', (100, 100), color='red')
        test_image_path = os.path.join(str(root), "test_profile.png")
        test_image.save(test_image_path)
        
        try:
            mock_get_names.return_value = ["Test Profile"]
            mock_get_content.return_value = test_image_path
            
            view = ProfileSelectionView(root)
            profile_button = view.winfo_children()[1]
            view.profile_button_hover(None, profile_button, test_image, "Test Profile")
            assert profile_button.cget('text') == "Test Profile"
            assert profile_button.cget('compound') == "center"
        finally:
            # Clean up the test image
            if os.path.exists(test_image_path):
                os.remove(test_image_path)

    @patch('controllers.ProfileController.get_profile_names')
    @patch('controllers.ProfileController.get_profile_content_by_line_number')
    def test_profile_button_leave(self, mock_get_content, mock_get_names, root):
        # Create a test image
        test_image = Image.new('RGB', (100, 100), color='red')
        test_image_path = os.path.join(str(root), "test_profile.png")
        test_image.save(test_image_path)
        
        try:
            mock_get_names.return_value = ["Test Profile"]
            mock_get_content.return_value = test_image_path
            
            view = ProfileSelectionView(root)
            profile_button = view.winfo_children()[1]
            view.profile_button_leave(None, profile_button, test_image)
            assert profile_button.cget('text') == " "
            assert profile_button.cget('compound') == "top"
        finally:
            # Clean up the test image
            if os.path.exists(test_image_path):
                os.remove(test_image_path)

    @patch('gui.FrameManager.load_frame')
    @patch('gui.Frames')
    def test_create_new_profile(self, mock_frames, mock_load_frame, root):
        # Set up mocks
        mock_frames.PROFILE_CREATION = 'PROFILE_CREATION'
        
        view = ProfileSelectionView(root)
        view.create_new_profile()
        
        mock_load_frame.assert_called_once_with(root, mock_frames.PROFILE_CREATION)

