from core.factories import Factory


class UserFactory(Factory):
    def create(self, **kwargs):
        return self.entity(
            username=kwargs.get('username'),
            email=kwargs.get('email'),
            password=kwargs.get('password', ""),
            is_active=kwargs.get("is_active")
        )