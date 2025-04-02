

class ApplicationGroup:
    def __init__(
            self, application_name: str,
            password: str, image: str = "") -> None:
        self.application_name = application_name
        self.password = password
        self.image = image
