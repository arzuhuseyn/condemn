from dataclasses import dataclass


@dataclass
class Entity:

    def __get_fields(self):
        return self.__dataclass_fields__.keys()