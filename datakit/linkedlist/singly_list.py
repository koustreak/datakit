#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: Node
Description: This is the ADT implementation of a singly linked list
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 28-Aug-2024
Version: 1.0.1
License: MIT License
Usage:
    - singly_list.py
Dependencies: None

Change History:
    - 28-Aug-2024: Initial Version of the script
"""

from typing import (
    List,
    TYPE_CHECKING,
    Tuple,
    Set
)

if TYPE_CHECKING:
    from datakit.linkedlist.node import SinglyNode

from datakit.exceptions.list_exception import HeadNodeException
from datakit.exceptions.list_exception import InvalidParameter
from datakit.exceptions.list_exception import ListIsEmpty
from datakit.linkedlist.node import SinglyNode

class InitSinglyList(object):

    def __init__(self) -> None:

        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_head(self) -> SinglyNode:
        return self.__head

    def set_head(self, node: SinglyNode) -> None:
        self.__head = node

    def get_size(self) -> int:
        return self.__size

    def set_size(self, size: int) -> None:
        self.__size = size

    def insert_rear(self, node: SinglyNode) -> bool:

        if self.get_head() is None:
            print('Head is None , please use insert_front')
            return False
        else:
            current = self.get_head()
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(node)
            self.set_size(self.get_size() + 1)
            return True

    def insert_front(self, node: SinglyNode) -> bool:

        if self.get_head() is None:
            self.set_head(node)
        else:
            node.set_next(self.get_head())
            self.set_head(node)
        self.set_size(self.get_size() + 1)
        return True

    def insert_middle(self, pos: int, node: SinglyNode) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='insert_middle')
        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')
        if pos > self.get_size() or pos < 0:
            reason = f'Out of Bound exception , valid range > 0 and < {self.get_size()}'
            raise InvalidParameter(reason, 'position', pos, method='insert_middle')

        if pos == 0:
            self.insert_front(node)
        elif pos == self.get_size():
            self.insert_rear(node)
        else:
            current = self.get_head()
            count = 0
            while count < pos:
                current = current.get_next()
                count += 1
            node.set_next(current.get_next())
            current.set_next(node)
            self.set_size(self.get_size() + 1)
            return True

    def update_by_value(self, prev_value, curr_value) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='update_value')
        current = self.get_head()
        update_count = 0
        while current is not None:
            if current.get_data() == prev_value:
                current.set_data(curr_value)
                update_count += 1
            current = current.get_next()
        if update_count:
            return True
        return False

    def update_by_pos(self, pos: int, curr_value) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='update_value')
        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')
        if pos > self.get_size() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range > 0 and < {self.get_size()}'
            raise InvalidParameter(reason, 'position', pos, method='update_value_at_pos')

        current = self.get_head()
        pos_count = 0
        while current is not None:
            if pos == pos_count:
                current.set_data(curr_value)
                return True
            current = current.get_next()
            pos_count += 1
        return False

    def delete_front(self) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='update_value')
        else:
            self.set_head(self.get_head().get_next())
            self.set_size(self.get_size()-1)
            return True

    def delete_rear(self) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='update_value')

        if self.get_size() == 1:
            self.delete_front()
        else:
            current = self.get_head()
            prev = None
            while current.get_next() is not None:
                prev = current
                current = current.get_next()
            prev.set_next(None)
            self.set_size(self.get_size() - 1)
            return True

    def delete_middle(self, pos: int) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='delete_middle')

        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

        if pos > self.get_size() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range > 0 and < {self.get_size()}'
            raise InvalidParameter(reason, 'position', pos, method='delete_middle')

        if pos == 0:
            self.delete_front()
        elif pos == self.get_size()-1:
            self.delete_rear()
        else:
            current = self.get_head()
            prev = self.get_head()
            count = 0
            if pos == 0:
                self.delete_front()
            elif pos == self.get_size() - 1:
                self.delete_rear()
            else:
                while count != pos:
                    prev = current
                    current = current.get_next()
                    count += 1
                prev.set_next(current.get_next())
                self.set_size(self.get_size() - 1)
            return True

    def pprint(self) -> None:

        if self.get_head() is None:
            raise HeadNodeException(method='update_value')

        current = self.get_head()
        while current is not None:
            if current.get_next() is not None:
                print(current.get_data(),end='->')
            else:
                print(current.get_data())
            current = current.get_next()

    def reverse(self):

        if self.get_head() is None:
            raise HeadNodeException(method='update_value')

        current = self.get_head()
        prev = None
        while current is not None:
            next_node = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_node
        self.set_head(prev)

    def reversed(self) -> 'InitSinglyList':
        new_list = self.__class__()
        current = self.get_head()
        while current is not None:
            new_node = SinglyNode(current.get_data())
            if new_list.get_head() is None:
                new_list.set_head(new_node)
            else:
                new_node.set_next(new_list.get_head())
                new_list.set_head(new_node)
            current = current.get_next()
        return new_list

    def __get_stat(self,choice) -> object:

        if self.get_head() is None:
            raise HeadNodeException(method='update_value')

        current = self.get_head()
        elements = []

        while current is not None:
            elements.append(current.get_data())
            current = current.get_next()
        if choice == 'min':
            return min(elements)
        if choice == 'max':
            return max(elements)
        if choice == 'avg':
            return sum(elements) / len(elements)

    def get_max(self) -> object:

        return self.__get_stat('max')

    def get_min(self) -> object:

        return self.__get_stat('min')

    def get_avg(self) -> object:

        return self.__get_stat('avg')

    def is_empty(self) -> bool:
        return self.get_head() is None

    @staticmethod
    def __create_from_collection(collection,_type:str) -> 'InitSinglyList':
        if not collection:
            raise ValueError('Collection of type '+str(_type)+' is empty , '
                                                              'hence can not create linkedlist from it')
        linkedlist = InitSinglyList()
        for i in collection:
            node = SinglyNode(i)
            if linkedlist.get_head() is None:
                linkedlist.set_head(node)
                linkedlist.set_size(linkedlist.get_size()+1)
            else:
                linkedlist.insert_rear(node)
        return linkedlist

    @staticmethod
    def from_list(input_list: List) -> 'InitSinglyList':

        if not isinstance(input_list, list):
            raise TypeError('Input collection must be of type list')
        return InitSinglyList.__create_from_collection(input_list,'list')

    @staticmethod
    def from_tuple(input_tuple: Tuple) -> 'InitSinglyList':

        if not isinstance(input_tuple, tuple):
            raise TypeError('Input collection must be of type list')
        return InitSinglyList.__create_from_collection(input_tuple,'tuple')

    @staticmethod
    def from_set(input_set: Set) -> 'InitSinglyList':

        if not isinstance(input_set, set):
            raise TypeError('Input collection must be of type set')
        return InitSinglyList.__create_from_collection(input_set,'set')







