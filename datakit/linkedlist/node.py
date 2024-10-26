#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: Node
Description: This is the ADT implementation of a singly linked list node and doubly linked list node.
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 26-Aug-2024
Version: 1.0.1
License: MIT License
Usage:
    - singly_list.py, doubly_list.py
Dependencies: None

Change History:
    - 26-Aug-2024: Initial Version of the script
"""


class SinglyNode(object):

    def __init__(self, data,next_node=None) -> None:

        if not data:
            raise ValueError('data is empty')
        self.__data = data
        self.__next = next_node

    def setdata(self, data) -> None:

        self.__data = data

    def getdata(self) -> object:

        return self.__data

    def setnext(self, next_node: object) -> None:

        self.__next = next_node

    def getnext(self) -> 'SinglyNode':

        return self.__next

    def hasnext(self) -> bool:

        return self.__next is not None

    def hasdata(self) -> bool:

        return self.__data is not None


class DoublyNode(object):

    def __init__(self, data, prev=None, next_node=None) -> None:

        self.__data = data
        self.__next = next_node
        self.__prev = prev

    def setdata(self, data) -> None:

        self.__data = data

    def getdata(self) -> object:

        return self.__data

    def setnext(self, next_node: object) -> None:

        self.__next = next_node

    def getnext(self) -> 'DoublyNode':

        return self.__next

    def setprev(self, prev_node: object) -> None:

        self.__prev = prev_node

    def getprev(self) -> 'DoublyNode':

        return self.__prev

    def hasnext(self) -> bool:

        return self.__next is not None

    def hasprev(self) -> bool:

        return self.__prev is not None

    def hasdata(self) -> object:

        return self.__data is not None