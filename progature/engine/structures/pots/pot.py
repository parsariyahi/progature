from __future__ import annotations
from typing import Iterable, Any


class Pot:

    def __init__(self, items: Iterable[Any]):
        self.items = items

    def __str__(self) -> str:
        string = " - ".join(str(item) for item in self.items)

        return string

    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index > len(self.items) - 1:
            raise StopIteration
        
        item = self.items[self._index]
        self._index += 1

        return item