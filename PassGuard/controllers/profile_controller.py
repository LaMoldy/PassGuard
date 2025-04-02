from utils import FileSystemHandler, FileSystemError

class ProfileController:
    @staticmethod
    def _get_profile_content(directory_path: str, profile_name: str) -> list[str]:
        """
        Gets the content of a profile from a profile file

        Args:
            directory_path (str): The path to the profiles directory
            profile_name (str): The name of the profile file

        Returns:
            list[str]: The content of the profile
        """
        profile_content_lines = []
        profile_content, error = FileSystemHandler.read_file(f"{directory_path}{profile_name}.profile")
        if error is FileSystemError.NONE:
            profile_content_lines = profile_content.splitlines()
        return profile_content_lines

    @staticmethod
    def get_profile_names(directory_path: str) -> list[str]:
        """
        Gets the profile names from all of the profile file

        Args:
            directory_path (str): The path to the profiles directory

        Returns:
            list[str]: The profile names
        """
        profile_files, error = FileSystemHandler.list_files_in_directory(directory_path)
        profile_names = []
        if error is FileSystemError.NONE:
            for i in range(len(profile_files)):
                profile_files[i] = profile_files[i].replace("_", " ")
                profile_names.append(profile_files[i].split(".")[0])
        return profile_names

    @staticmethod
    def get_profile_content_by_line_number(directory_path: str, profile_name: str, line_number: int) -> str:
        """
        Gets the specific line of a profile file

        Args:
            directory_path (str): The path to the profiles directory
            profile_name (str): The name of the profile file
            line_number (int): The line number to get the content from

        Returns:
            str: The content of the specific line from the profile
        """
        profile_content_lines = ProfileController._get_profile_content(directory_path, profile_name)
        if line_number >= len(profile_content_lines):
            return ""
        elif len(profile_content_lines) > 0:
            return profile_content_lines[line_number]
        return ""

    @staticmethod
    def create_profile(directory_path: str, profile_name: str, content: str) -> FileSystemError:
        """
        Creates a profile file with the provided content

        Args:
            directory_path (str): The path to the profiles directory
            profile_name (str): The name of the profile file
            content (str): The content of the profile
        Returns:
            FileSystemError: An error if any occur
        """
        return FileSystemHandler.create_file(f"{directory_path}{profile_name}.profile", content)

    @staticmethod
    def add_to_profile(directory_path: str, profile_name: str, content: str) -> FileSystemError:
        """
        Adds content to a profile file

        Args:
            directory_path (str): The path to the profiles directory
            profile_name (str): The name of the profile file
            content (str): The content of the profile
        Returns:
            FileSystemError: An error if any occur
        """
        return FileSystemHandler.append_content_to_file(f"{directory_path}{profile_name}.profile", content)
