#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: BaseException
Description: This is the parent class of all util for datakit
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 27-Aug-2024
Version: 1.0
License: MIT License
Inheritance: linkedlist.py , StackException.py
Dependencies: None

Change History:
    - 27-Aug-2024: Initial Version of the script
"""

import warnings
from typing import *
from datakit.util.console_print import bcolors
from datakit.linkedlist.node import DoublyNode
from datakit.util.exception.linkedlist import (
    InvalidParameter,
    HeadNodeException,
    BrokenLinkException
)

class InitDoublyList(object):

    def __init__(self):

        self.__head = None
        self.__size = 0

    def set_head(self, head:DoublyNode) -> None:
        self.__head = head

    def get_head(self) -> DoublyNode:
        return self.__head

    def set_size(self, size: int) -> None:
        self.__size = size

    def get_size(self) -> int:
        return self.__size

    def insert_front(self, node:DoublyNode) -> bool:
        if self.get_head() is None:
            self.set_head(node)
        else:
            current_head = self.get_head()
            current_head.set_prev(node)
            node.set_next(current_head)
            self.set_head(node)
        self.set_size(self.get_size() + 1)
        return True

    def insert_rear(self, node:DoublyNode) -> bool:
        if self.get_head() is None:
            print(bcolors.WARNING + 'As Head is None , the input node will be set as head node ' + bcolors.ENDC)
            self.set_head(node)
        else:
            current = self.get_head()
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(node)
            node.set_prev(current)
        self.set_size(self.get_size() + 1)
        return True

    def insert_middle(self,pos:int, node:DoublyNode) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='insert_middle')

        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

        if pos > self.get_size() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range is 0 to {self.get_size() - 1}'
            raise InvalidParameter(reason, 'position', pos, method='insert_middle')

        if pos == 0 :
            self.insert_front(node)
        else:
            current = self.get_head()
            count = 0
            while count < pos:
                current = current.get_next()
                count += 1

            node.set_next(current.get_next())
            current.get_next().set_prev(node)
            current.set_next(node)
            node.set_prev(current)

            self.set_size(self.get_size() + 1)
            return True

    def delete_front(self) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='delete_front')
        else:
            self.set_head(self.get_head().get_next())
            self.set_size(self.get_size()-1)
            return True

    def delete_rear(self) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='delete_rear')

        if self.get_size() == 1:
            self.delete_front()
        else:
            current = self.get_head()
            prev = self.get_head()
            while current.get_next() is not None:
                prev = current
                current = current.get_next()
            prev.set_next(None)
            self.set_size(self.get_size() - 1)
            return True

    def delete_middle(self, pos: int) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='delete_middle')

        if pos > self.get_size() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range is 0 to {self.get_size() - 1}'
            raise InvalidParameter(reason, 'position', pos, method='delete_middle')

        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

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
            current.get_next().set_prev(prev)
        self.set_size(self.get_size() - 1)
        return True

    def update_by_value(self,prev_value,updated_value) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='update_by_value')

        current = self.get_head()
        update_count = 0
        while current is not None:
            if current.get_data() == prev_value:
                current.set_data(updated_value)
                update_count += 1
        if update_count:
            return True
        return False

    def update_by_pos(self, pos:int, updated_value) -> bool:

        if self.get_head() is None:
            raise HeadNodeException(method='update_by_pos')

        if pos > self.get_size() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range is 0 to {self.get_size() - 1}'
            raise InvalidParameter(reason, 'position', pos, method='update_by_pos')
        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

        cur_node = self.get_head()
        cur_pos = 0
        while cur_node is not None:
            if cur_pos == pos:
                cur_node.set_data(updated_value)
                return True
            cur_node = cur_node.get_next()
            cur_pos += 1
        return False

    def pprint(self) -> None:

        if self.get_head() is None:
            warnings.warn('HeadNode is None , can not print LinkedList')

        current = self.get_head()
        while current is not None:
            if current.get_next() is not None:
                if current.get_next().get_prev() == current:
                    print(current.get_data(),end=' <--> ')
                else:
                    raise BrokenLinkException(msg='can not print linkedlist',method='pprint')
            else:
                print(current.get_data())
            current = current.get_next()

    def reverse(self):

        if self.get_head() is None:
            raise HeadNodeException(method='reverse')

        current = self.get_head()
        while current.get_next() is not None:
            next_node = current.get_next()
            current.set_prev(next_node)
            current = next_node
        self.set_head(current)

    def reversed(self) -> 'InitDoublyList':
        new_list = self.__class__()
        current = self.get_head()
        while current is not None:
            new_node = DoublyNode(current.get_data())
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

    @staticmethod
    def __create_from_collection(collection,_type:str) -> 'InitDoublyList':

        if not collection:
            raise ValueError('Collection Object '+_type+' is empty')

        linkedlist = InitDoublyList()
        for i in collection:
            node = DoublyNode(i)
            if linkedlist.get_head() is None:
                linkedlist.set_head(node)
                linkedlist.set_size(linkedlist.get_size() + 1)
            else:
                linkedlist.insert_rear(node)
        return linkedlist

    @staticmethod
    def from_list(input_list: List) -> 'InitDoublyList':

        if not isinstance(input_list, list):
            raise TypeError('Input collection must be of type list')
        return InitDoublyList.__create_from_collection(input_list, 'list')

    @staticmethod
    def from_tuple(input_tuple: Tuple) -> 'InitDoublyList':

        if not isinstance(input_tuple, tuple):
            raise TypeError('Input collection must be of type list')
        return InitDoublyList.__create_from_collection(input_tuple, 'tuple')

    @staticmethod
    def from_set(input_set: Set) -> 'InitDoublyList':

        if not isinstance(input_set, set):
            raise TypeError('Input collection must be of type set')
        return InitDoublyList.__create_from_collection(input_set, 'set')




























    