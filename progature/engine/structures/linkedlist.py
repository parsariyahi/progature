from __future__ import annotations
from typing import Union
import uuid

from progature.engine.structures import Node

class DLinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value) -> None:
        node = Node(value)
        node.next_node = None

        if self.head is None:
            node.prev_node = None
            self.head = node
            return

        last = self.head
        while last.next_node is not None:
            last = last.next_node

        last.next_node = node
        node.prev_node = last
        return

    def __str__(self) -> str:
        result = ""
        pointer = self.head

        while pointer is not None:
            result += (str(pointer.id) + " -> ")
            pointer = pointer.next_node

        return result