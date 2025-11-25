from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name.replace("_", " ").title()) for choice in cls]
