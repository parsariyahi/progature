from __future__ import annotations
from typing import Union
import uuid

class Node:
    def __init__(self, data, next_node: Union[Node | None] = None, prev_node: Union[Node | None] = None) -> None:
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
        self.id = uuid.uuid1().int

    def __str__(self) -> str:
        return str(self.id)

    def __eq__(self, other: Node) -> bool:
        if not(isinstance(other, Node)):
            raise ValueError(f"Two object ({self} , {other}) are not the same Type")

        return self.id == other.id