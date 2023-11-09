from typing import Dict


class Skill:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        if isinstance(other, Skill):
            return self.name == other.name

        raise TypeError("Type Error Skill")

    def as_dict(self) -> Dict:
        return {
            "name": self.name,
        }
