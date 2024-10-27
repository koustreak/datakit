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

    def set_data(self, data) -> None:

        self.__data = data

    def get_data(self) -> object:

        return self.__data

    def set_next(self, next_node: object) -> None:

        self.__next = next_node

    def get_next(self) -> 'SinglyNode':

        return self.__next

    def has_next(self) -> bool:

        return self.__next is not None

    def has_data(self) -> bool:

        return self.__data is not None


class DoublyNode(object):

    def __init__(self, data, prev=None, next_node=None) -> None:

        self.__data = data
        self.__next = next_node
        self.__prev = prev

    def set_data(self, data) -> None:

        self.__data = data

    def get_data(self) -> object:

        return self.__data

    def set_next(self, next_node: object) -> None:

        self.__next = next_node

    def get_next(self) -> 'DoublyNode':

        return self.__next

    def set_prev(self, prev_node: object) -> None:

        self.__prev = prev_node

    def get_prev(self) -> 'DoublyNode':

        return self.__prev

    def has_next(self) -> bool:

        return self.__next is not None

    def has_prev(self) -> bool:

        return self.__prev is not None

    def has_data(self) -> object:

        return self.__data is not None