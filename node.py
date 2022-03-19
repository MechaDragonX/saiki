#!/usr/bin/env python

from typing import TypeVar, Generic

T = TypeVar('T')

# Type probably refers to the chars in the case of strings, since each node contains a char
class Node(Generic[T]):
    def __init__(self, value, isTerminal, isHead):
        self.value = value
        self.isTerminal = isTerminal
        if isHead:
            self.value = '@'
