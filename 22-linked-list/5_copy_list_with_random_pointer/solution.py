from typing import Optional


class Node:
    def __init__(self, val: int, next: "Node" = None, random: "Node" = None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    return None
