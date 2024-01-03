from typing import Dict


__all__ = [
    "Skill",
]


class Skill:
    def __init__(self, name) -> None:
        """Skill component contains quest data of each skill in game,
        This Class is universal interface for Skill all over the app.
        We just work with this class when we intract with our Skills.

        Parameters
        ----------
        name : string
            The name of skill.
        """
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        if isinstance(other, Skill):
            return self.name == other.name

        raise TypeError("Type Error Skill")

    def as_dict(self) -> Dict:
        """Returns the `dict` representation of `Skill` object.

        Returns
        -------
        dict
            The representation of the `Skill`.

        Examples
        --------
        ```python
        >>> s = Skill("NAME")
        >>> s.as_dict()
        {
            "name": NAME,
        }
        ```
        """
        return {
            "name": self.name,
        }
