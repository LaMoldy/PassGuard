import pytest
from customtkinter import CTk
from gui.frame_manager import FrameManager, Frames
from gui.views import ProfileSelectionView

class TestFrameManager:
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
