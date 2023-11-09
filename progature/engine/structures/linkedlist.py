from __future__ import annotations
from typing import Union, Iterable
import uuid

from progature.engine.structures import Node


class DLinkedList:
    def __init__(self, items: Iterable):
        self.head = None
        for item in items:
            self.insert(item)

    def insert(self, value) -> None:
        node = Node(value)

        if self.head is None:
            node.prev_node = None
            self.head = node
            return

        node.next_node = self.head
        self.head = node

        # last = self.head
        # while last.next_node is not None:
        #     last = last.next_node

        # last.next_node = node
        # node.prev_node = last
        return

    def __str__(self) -> str:
        result = ""
        pointer = self.head

        while pointer is not None:
            result += " < - " + str(pointer.data) + " -> "
            pointer = pointer.next_node

        return result
