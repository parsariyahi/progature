from typing import Dict


class Quest:
    def __init__(self, index: int, name, is_complete=False):
        """Quest component contains quest data of each quest in game,
        This Class is universal interface for Quest all over the app.
        We just work with this class when we intract with our Quests.

        Parameters
        ----------
        index: int
            The index of each quest inside quest list in "".json"" file

        name : string
            The name of quest.

        is_complete : bool, optional
            Status of quest completion
        """
        self.index = index
        self.name = name
        self.is_complete = is_complete

    def __str__(self) -> str:
        string = f"{self.index}.{self.name}:{self.is_complete}"
        return string

    def __eq__(self, other) -> bool:
        if isinstance(other, Quest):
            return self.name == other.name

        raise TypeError("Type Error Quest")

    def as_dict(self) -> Dict:
        return {
            "index": self.index,
            "name": self.name,
            "is_complete": self.is_complete,
        }
