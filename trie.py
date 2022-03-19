#!/usr/bin/env python

from typing import TypeVar, Generic
from node import Node

T = TypeVar('T')

# Type probably refers to the chars in the case of strings, since each node contains a char
class Trie(Generic[T]):
    def __init__(self, value):
        self.head = Node(value, False, True)
        self.next = None
