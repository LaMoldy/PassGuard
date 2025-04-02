from models import ApplicationGroup

class Profile:
    def __init__(
            self, name: str, password: str,
            profile_image: str, application_groups: list[ApplicationGroup]) -> None:
        self.name = name
        self.password = password
        self.profile_image = profile_image
        self.application_groups = application_groups
