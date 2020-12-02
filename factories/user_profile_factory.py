from core.factories import Factory


class UserProfileFactory(Factory):
    def create(self, **kwargs):
        return self.entity(
            user=kwargs.get('user'),
            name=kwargs.get('name'),
            surname=kwargs.get('surname'),
            image=kwargs.get('image')
        )