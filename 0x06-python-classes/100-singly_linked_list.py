#!/usr/bin/python3
"""defines a singly linked list"""


class Node:
    """A Node"""
    def __init__(self, data, next_node=None):
        """Node constructor"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

        @property
        def data(self):
            """returns data"""
            return self.__data

        @property
        def next_node(self):
            """returns next node"""
            return self.__next_node

        @data.setter
        def data(self, data):
            """sets data"""
            if type(data) is not int:
                raise TypeError("data must be an integer")
            self.__data = data

        @next_node.setter
        def next_node(self, n):
            """returns next node"""
            if n is not None and type(n) is not Node:
                raise TypeError("next_node must be a Node object")
            self.__next_node = n


class SinglyLinkedList:
    """defines list"""
    def __init__(self):
        """list  constructor"""
        self.__head = Node()

    def __str__(self):
        """prints list"""
        pass

    def sorted_insert(self, value):
        """performs sorted insert on list"""
        pass
