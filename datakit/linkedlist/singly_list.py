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

from typing import *
from datakit.exceptions.console_print import bcolors
from datakit.exceptions.list_exception import HeadNodeException
from datakit.exceptions.list_exception import InvalidParameter
from datakit.linkedlist.node import SinglyNode

class InitSinglyList(object):

    def __init__(self) -> None:

        self.__head = None
        self.__size = 0

    def gethead(self) -> SinglyNode:
        return self.__head

    def getsize(self) -> int:
        return self.__size

    def setsize(self, size: int) -> None:
        self.__size = size

    def sethead(self, node: SinglyNode) -> None:
        self.__head = node

    def insert_rear(self, node: SinglyNode) -> bool:

        if self.gethead() is None:
            print(bcolors.WARNING+'As Head is None , please use insert_at_start '+bcolors.ENDC)
            return False
        else:
            current = self.gethead()
            while current.getnext() is not None:
                current = current.getnext()
            current.setnext(node)
            self.setsize(self.getsize() + 1)
            return True

    def insert_front(self, node: SinglyNode) -> bool:

        if self.gethead() is None:
            self.sethead(node)
        else:
            node.setnext(self.gethead())
            self.sethead(node)
        self.setsize(self.getsize() + 1)
        return True

    def insert_middle(self, pos: int, node: SinglyNode) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='insert_middle')
        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')
        if pos > self.getsize() or pos < 0:
            reason = f'Out of Bound exception , valid range > 0 and < {self.getsize()}'
            raise InvalidParameter(reason, 'position', pos, method='insert_middle')

        if pos == 0:
            self.insert_front(node)
        elif pos == self.getsize():
            self.insert_rear(node)
        else:
            current = self.gethead()
            count = 0
            while count < pos-1:
                current = current.getnext()
                count += 1
            node.setnext(current.getnext())
            current.setnext(node)
            self.setsize(self.getsize() + 1)
            return True

    def update_by_value(self, prev_value, curr_value) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')
        current = self.gethead()
        update_count = 0
        while current is not None:
            if current.getdata() == prev_value:
                current.setdata(curr_value)
                update_count += 1
            current = current.getnext()
        if update_count:
            return True
        return False

    def update_by_pos(self, pos: int, curr_value) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')
        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')
        if pos > self.getsize() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range > 0 and < {self.getsize()}'
            raise InvalidParameter(reason, 'position', pos, method='update_value_at_pos')

        current = self.gethead()
        pos_count = 0
        while current is not None:
            if pos == pos_count:
                current.setdata(curr_value)
                return True
            current = current.getnext()
            pos_count += 1
        return False

    def delete_front(self) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')
        else:
            self.sethead(self.gethead().getnext())
            self.setsize(self.getsize()-1)
            return True

    def delete_rear(self) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')

        if self.getsize() == 1:
            self.delete_front()
        else:
            current = self.gethead()
            prev = None
            while current.getnext() is not None:
                prev = current
                current = current.getnext()
            prev.setnext(None)
            self.setsize(self.getsize() - 1)
            return True

    def delete_middle(self, pos: int) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='delete_middle')

        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

        if pos > self.getsize() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range > 0 and < {self.getsize()}'
            raise InvalidParameter(reason, 'position', pos, method='delete_middle')

        if pos == 0:
            self.delete_front()
        elif pos == self.getsize()-1:
            self.delete_rear()
        else:
            current = self.gethead()
            prev = self.gethead()
            count = 0
            if pos == 0:
                self.delete_front()
            elif pos == self.getsize() - 1:
                self.delete_rear()
            else:
                while count != pos:
                    prev = current
                    current = current.getnext()
                    count += 1
                prev.setnext(current.getnext())
                self.setsize(self.getsize() - 1)
            return True

    def pprint(self) -> None:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')

        current = self.gethead()
        while current is not None:
            if current.getnext() is not None:
                print(current.getdata(),end='->')
            else:
                print(current.getdata())
            current = current.getnext()

    def reverse(self) -> SinglyNode:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')

        current = self.gethead()
        prev = None
        while current is not None:
            next_node = current.getnext()
            current.setnext(prev)
            prev = current
            current = next_node
        self.sethead(prev)

    def reversed(self) -> 'InitSinglyList':
        new_list = self.__class__()
        current = self.gethead()
        while current is not None:
            new_node = SinglyNode(current.getdata())
            if new_list.gethead() is None:
                new_list.sethead(new_node)
            else:
                new_node.setnext(new_list.gethead())
                new_list.sethead(new_node)
            current = current.getnext()
        return new_list

    def __get_stat(self,choice) -> object:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')

        current = self.gethead()
        elements = []

        while current is not None:
            elements.append(current.getdata())
            current = current.getnext()
        if choice == 'min':
            return min(elements)
        if choice == 'max':
            return max(elements)
        if choice == 'avg':
            return sum(elements) / len(elements)

    def getmax(self) -> object:

        return self.__get_stat('max')

    def getmin(self) -> object:

        return self.__get_stat('min')

    def getavg(self) -> object:

        return self.__get_stat('avg')

    def is_empty(self) -> bool:
        return self.gethead() is None

    @staticmethod
    def __create_from_collection(collection,_type:str) -> 'InitSinglyList':
        if not collection:
            raise ValueError('Collection of type '+str(_type)+' is empty , '
                                                              'hence can not create linkedlist from it')
        linkedlist = InitSinglyList()
        for i in collection:
            node = SinglyNode(i)
            if linkedlist.gethead() is None:
                linkedlist.sethead(node)
                linkedlist.setsize(linkedlist.getsize()+1)
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







