from __future__ import annotations
from typing import Optional, Union, Dict

from progature.engine.structures import Pot
from progature.engine.components.skill import Skill
from progature.engine.components.chapter import Chapter


__all__ = [
    "Game",
]


class Game:
    def __init__(
        self,
        file_name: str,
        name: str,
        skill: Optional[Skill | None] = None,
        chapters: Optional[Pot[Chapter] | None] = None,
        is_complete=False,
    ) -> None:
        """Game component contains all the game data in single obj,
        This Class is universal interface for Games all over the app.
        We just work with this class when we intract with our Games.

        Parameters
        ----------
        file_name: string
            The path of "".json"" file of the game.
        name : string
            The name of game.
        skill : Skill or None, optional
            Skill of each game.
        chapters : Pot[Chapter] or None, optional
            Chapters of each game.
        is_complete : bool, optional
            Status of game completion
        """
        self.file_name: str = file_name
        self.name: str = name
        self.skill: Skill = skill
        self.chapters: Pot[Chapter] = chapters
        self.is_complete: bool = is_complete

    def __str__(self) -> str:
        string = f"{self.name}:{self.is_complete}"
        return string

    def __eq__(self, other) -> bool:
        if isinstance(other, Game):
            return self.name == other.name

        raise TypeError("Type Error Game")

    def as_dict(self) -> Dict:
        """Returns the `dict` representation of `Game` object.

        Returns
        -------
        dict
            The representation of the `Game`.

        Examples
        --------
        ```python
        >>> g = Game("FILE_NAME", "NAME", "SKILL", "IS_COMPLETE", "CHAPTERS")
        >>> g.as_dict()
        {
            "file_name": FILE_NAME,
            "name": NAME,
            "skill": SKILL,
            "is_complete": IS_COMPLETE,
            "chapters": CHAPTERS,
        }
        ```
        """
        return {
            "file_name": self.file_name,
            "name": self.name,
            "skill": self.skill.name if self.skill else "",
            "is_complete": self.is_complete,
            "chapters": [chapter.as_dict() for chapter in self.chapters] if self.chapters else [],
        }

    @property
    def skill(self) -> Union[Skill, None]:
        """Skill property

        Returns
        -------
        Skill or None
            Returns the `Skill` object of the `Game` or `None`.
        """
        return self._skill

    @skill.setter
    def skill(self, skill: Optional[Skill | None]):
        self._skill = skill

    @property
    def chapters(self) -> Union[Pot[Chapter], None]:
        """`chapters` property

        Returns
        -------
        Pot[Chapter] or None
            Returns the `Pot` object that contains `Chapter`'s of the `Game` or `None`.
        """
        return self._chapters

    @chapters.setter
    def chapters(self, chapters: Optional[Pot[Chapter] | None]):
        self._chapters = chapters
