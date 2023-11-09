from __future__ import annotations
from typing import Iterable, Any, Generic, TypeVar

Game = TypeVar("Game")
Skill = TypeVar("Skill")
Chapter = TypeVar("Chapter")
Level = TypeVar("Level")
Quest = TypeVar("Quest")

T = TypeVar("T", Game, Skill, Chapter, Level, Quest)


class Pot(Generic[T]):
    def __init__(self, items: Iterable[T]):
        self.items = items

    def __str__(self) -> str:
        string = " - ".join(str(item) for item in self.items)

        return string

    def __getitem__(self, index: int) -> T:
        return self.items[index]

    def __iter__(self):
        self._index: int = 0
        return self

    def __next__(self) -> T:
        if self._index > len(self.items) - 1:
            raise StopIteration

        item: T = self.items[self._index]
        self._index += 1

        return item
