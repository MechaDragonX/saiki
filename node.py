#!/usr/bin/env python

class Node():
    def __init__(self, value, isTerminal, isHead):
        self.__value = value
        self.__isHead = isHead
        if isHead:
            self.value = '@'
        self.__isTerminal = isTerminal
        if isTerminal:
            self.value = '*'
        self.__children = []



    def getChildren(self) -> list:
        return self.__children



    def getFirstChild(self):
        return self.__children[0]


    # def addToChildren(self, value):
    #     self.__children.append(value)
