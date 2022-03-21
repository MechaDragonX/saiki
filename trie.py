#!/usr/bin/env python

from node import Node

class Trie():
    def __init__(self, value):
        self.__head = Node(value, False, True)
        self.__children = []
    

    def __add_new_start_letter(self, start_index, value):
        if len(value) == 0:
            self.__children.append(Node(value[0], True, False))
        else:
            self.__children.append(Node(value[0], False, False))

        current = self.__children[start_index]
        for i in range(1, len(value)):
                current.get_children().append(Node(value[i], False, False))
                current = current.get_children()

        current.get_children().append(Node('', True, False))


    def add(self, value):
        # Only applies if there are already starting letters present
        add_letter = False
        start_index = 0

        if len(self.__children) == 0:
            self.__add_new_start_letter(0, value)

        else:
            for i in range(0, len(self.__children)):
                if self.__children[i] == value[0]:
                    add_letter = False
                    start_index = i

            if add_letter == True:
                self.__add_new_start_letter(len(self.__children), value)
            else:
                self.__append_to_start(start_index, value)
