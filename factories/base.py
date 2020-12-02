class Factory:

    def __init__(self, entity):
        self.entity=entity

    def create(self, **kwargs):
        """ Override this method """
        pass