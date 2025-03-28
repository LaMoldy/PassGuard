import os

class Profile():
    @staticmethod
    def create_profile(
        file_name: str, current_dir: str, profile_name: str,
        password: str, image_path: str
    ) -> tuple[str, bool]:
        msg, is_successful = Profile._create_profile_file(file_name, current_dir)
        if not is_successful:
            return msg, False

        msg, is_successful = Profile._write_profile_information(
            file_name,
            profile_name,
            password,
            image_path
        )
        if not is_successful:
            return msg, False

        return "", True

    @staticmethod
    def _create_profile_file(file_name: str, current_dir: str) -> tuple[str, bool]:
        from controllers import File

        if current_dir:
            file_name = current_dir + file_name

        is_successful = File.create(file_name)
        if not is_successful:
            return "Error creating profile", False

        return "", True

    @staticmethod
    def _write_profile_information(
        file_name: str, profile_name: str, password: str, image_path: str
    ) -> tuple[str, bool]:
        from controllers import File, Password

        hashed_password = Password.hash(password)
        file_content = f"{image_path}\n{profile_name}\n{str(hashed_password)}"

        is_successful = File.update(file_name, file_content)
        if not is_successful:
            return "Error writing profile", False

        return "", True

    @staticmethod
    def get_profile_file_names(profile_directory: str) -> list[str]:
        return [f.rsplit(".", 1)[0] for f in os.listdir(profile_directory) if f.endswith(".profile") and os.path.isfile(os.path.join(profile_directory, f))]

    @staticmethod
    def get_profile_pictures(profile_directory: str) -> list[str]:
        profile_pictures = []
        for filename in os.listdir(profile_directory):
            if filename.endswith(".profile"):
                file_path = os.path.join(profile_directory, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        image_path = file.readline().strip()
                        profile_pictures.append(image_path)
                except Exception as e:
                    return []
        return profile_pictures

    @staticmethod
    def count_profiles(profile_directory: str) -> int:
        return sum(1 for file in os.listdir(profile_directory) if file.endswith(".profile"))

    @staticmethod
    def get_profile_password(profile_directory: str, profile_name: str):
        from controllers import File
        file_path = os.path.join(profile_directory, profile_name + ".profile")
        content, error = File.read(file_path)
        if not error:
            return ""
        lines = content.splitlines()
        if len(lines) > 3:
            return lines[2]
        return ""