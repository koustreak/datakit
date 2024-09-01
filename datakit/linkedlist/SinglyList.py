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
    - SinglyList.py
Dependencies: None

Change History:
    - 28-Aug-2024: Initial Version of the script
"""

from typing import *
from datakit.exceptions.ConsolePrint import bcolors
from datakit.exceptions.ListException import NoneNodeException, HeadNodeException
from datakit.exceptions.ListException import InvalidParameter
from datakit.linkedlist.Node import SinglyNode

class SinglyLinkedList(object):

    def __init__(self) -> None:

        self.__head = None
        self.__size = 0

    def gethead(self) -> SinglyNode:

        return self.__head

    def getsize(self) -> int:

        return self.__size

    def setsize(self, size: int) -> None:

        self.__size = size

    def sethead(self, node: SinglyNode) -> bool:

        self.__head = node

    def insert_rear(self, node: SinglyNode) -> bool:

        if self.gethead() is None:
            print(bcolors.WARNING+'As Head is None , please use insert_at_start '+bcolors.ENDC)
            return False
        else:
            current = self.gethead()
            while current.getnext() is not None:
                current = current.getNext()
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

        if pos == 0 or pos == self.getsize() - 1:
            print(bcolors.WARNING + 'To insert at front or rear end of the linkedlist , '
                                    'please use insert_front and insert_rear ' + bcolors.ENDC)
            return False
        else:
            if pos > self.getsize() - 1 or pos < 0:
                reason = f'Out of Bound exception , valid range is 0 to {self.getsize() - 1}'
                raise InvalidParameter(reason,'position',pos,method='insert_middle')
            if not (isinstance(pos,int)):
                raise TypeError('Invalid value of pos parameter , it must be an integer')
            current = self.gethead()
            count = 0
            while count < pos-1:
                current = current.getnext()
                count += 1
            node.setnext(current.getnext())
            current.setnext(node)
            self.setsize(self.getsize() + 1)
            return True

    def update_value(self, prev_value, curr_value) -> bool:

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

    def update_value_at_pos(self, pos: int, curr_value) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')
        else:
            if pos > self.getsize() - 1 or pos < 0:
                reason = f'Out of Bound exception , valid range is 0 to {self.getsize() - 1}'
                raise InvalidParameter(reason, 'position', pos, method='update_value_at_pos')
            if not (isinstance(pos, int)):
                raise TypeError('Invalid value of pos parameter , it must be an integer')

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
            prev = self.gethead()
            while current.getnext() is not None:
                prev = current
                current = current.getnext()
            prev.setnext(None)
            self.setsize(self.getsize() - 1)
            return True

    def delete_middle(self, pos: int) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='delete_middle')

        if pos > self.getsize() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range is 0 to {self.getsize() - 1}'
            raise InvalidParameter(reason, 'position', pos, method='delete_at_pos')
        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

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

    def print_list(self) -> None:

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')

        current = self.gethead()
        while current is not None:
            if current.getnext() is not None:
                print(current.getdata(),end='->')
            else:
                print(current.getdata(),end='')
            current = current.getnext()

    def reverse(self,in_place=False) -> 'SinglyLinkedList':

        if self.gethead() is None:
            raise HeadNodeException(method='update_value')

        if in_place:
            current = self.gethead()
            prev = None
            while current is not None:
                next_node = current.getnext()
                current.setnext(prev)
                prev = current
                current = next_node
        else:
            new_list = self.__class__()
            current = self.gethead()
            while current is not None:
                if new_list.gethead() is None:
                    new_list.sethead(current)
                else:
                    current.setnext(new_list.gethead())
                    new_list.sethead(current)
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

    @staticmethod
    def __create_linkedlist_from_collection(collection,_type:str) -> 'SinglyLinkedList':

        linkedlist = SinglyLinkedList()
        for i in collection:
            node = SinglyNode(i)
            if linkedlist.gethead() is None:
                linkedlist.sethead(node)
            else:
                linkedlist.insert_rear(node)
        return linkedlist

    @staticmethod
    def from_list(input_list: List) -> 'SinglyLinkedList':

        if not isinstance(input_list, list):
            raise TypeError('Input collection must be of type list')
        return SinglyLinkedList.__create_linkedlist_from_collection(input_list,'list')

    @staticmethod
    def from_tuple(input_tuple: Tuple) -> 'SinglyLinkedList':

        if not isinstance(input_tuple, tuple):
            raise TypeError('Input collection must be of type list')
        return SinglyLinkedList.__create_linkedlist_from_collection(input_tuple,'tuple')

    @staticmethod
    def from_set(input_set: Set) -> 'SinglyLinkedList':

        if not isinstance(input_set, set):
            raise TypeError('Input collection must be of type set')
        return SinglyLinkedList.__create_linkedlist_from_collection(input_set,'set')







