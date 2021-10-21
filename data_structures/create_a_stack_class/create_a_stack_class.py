from __future__ import annotations
from typing import Any


class Stack:
    def __init__(self, lst: list = None) -> None:
        self.list = lst if lst else []

    def is_empty(self) -> bool:
        return not self.list

    def push(self, item: Any) -> Stack:
        self.list.append(item)
        return self

    def pop(self) -> Any:
        return self.list.pop() if self.list else None

    def peek(self) -> Any:
        return None if not self.list else self.list[-1]

    def clear(self) -> Stack:
        self.list = []
        return self

    def size(self) -> int:
        return len(self)

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)
