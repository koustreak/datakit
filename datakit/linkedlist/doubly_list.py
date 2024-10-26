#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: BaseException
Description: This is the parent class of all exceptions for datakit
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 27-Aug-2024
Version: 1.0
License: MIT License
Inheritance: list_exception.py , StackException.py
Dependencies: None

Change History:
    - 27-Aug-2024: Initial Version of the script
"""

import warnings
from typing import *
from datakit.exceptions.console_print import bcolors
from datakit.linkedlist.node import DoublyNode
from datakit.exceptions.list_exception import (
    InvalidParameter,
    HeadNodeException,
    BrokenLinkException
)

class InitDoublyList(object):

    def __init__(self):

        self.__head = None
        self.__size = 0

    def sethead(self, head:DoublyNode) -> None:
        self.__head = head

    def gethead(self) -> DoublyNode:
        return self.__head

    def setsize(self, size: int) -> None:
        self.__size = size

    def getsize(self) -> int:
        return self.__size

    def insert_front(self, node:DoublyNode) -> bool:
        if self.gethead() is None:
            self.sethead(node)
        else:
            current_head = self.gethead()
            current_head.setprev(node)
            node.setnext(current_head)
            self.sethead(node)
        self.setsize(self.getsize() + 1)
        return True

    def insert_rear(self, node:DoublyNode) -> bool:
        if self.gethead() is None:
            print(bcolors.WARNING + 'As Head is None , the input node will be set as head node ' + bcolors.ENDC)
            self.sethead(node)
        else:
            current = self.gethead()
            while current.getnext() is not None:
                current = current.getnext()
            current.setnext(node)
            node.setprev(current)
        self.setsize(self.getsize() + 1)
        return True

    def insert_middle(self,pos:int, node:DoublyNode) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='insert_middle')

        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

        if pos > self.getsize() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range is 0 to {self.getsize() - 1}'
            raise InvalidParameter(reason, 'position', pos, method='insert_middle')

        if pos == 0 :
            self.insert_front(node)
        else:
            current = self.gethead()
            count = 0
            while count < pos-1:
                current = current.getnext()
                count += 1

            node.setnext(current.getnext())
            current.getnext().setprev(node)
            current.setnext(node)
            node.setprev(current)

            self.setsize(self.getsize() + 1)
            return True

    def delete_front(self) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='delete_front')
        else:
            self.sethead(self.gethead().getnext())
            self.setsize(self.getsize()-1)
            return True

    def delete_rear(self) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='delete_rear')

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
            raise InvalidParameter(reason, 'position', pos, method='delete_middle')

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
            current.getnext().setprev(prev)
        self.setsize(self.getsize() - 1)
        return True

    def update_by_value(self,prev_value,updated_value) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='update_by_value')

        current = self.gethead()
        update_count = 0
        while current is not None:
            if current.getdata() == prev_value:
                current.setdata(updated_value)
                update_count += 1
        if update_count:
            return True
        return False

    def update_by_pos(self, pos:int, updated_value) -> bool:

        if self.gethead() is None:
            raise HeadNodeException(method='update_by_pos')

        if pos > self.getsize() - 1 or pos < 0:
            reason = f'Out of Bound exception , valid range is 0 to {self.getsize() - 1}'
            raise InvalidParameter(reason, 'position', pos, method='update_by_pos')
        if not (isinstance(pos, int)):
            raise TypeError('Invalid value of pos parameter , it must be an integer')

        cur_node = self.gethead()
        cur_pos = 0
        while cur_node is not None:
            if cur_pos == pos:
                cur_node.setdata(updated_value)
                return True
            cur_node = cur_node.getnext()
            cur_pos += 1
        return False

    def pprint(self) -> None:

        if self.gethead() is None:
            warnings.warn('HeadNode is None , can not print LinkedList')

        current = self.gethead()
        while current is not None:
            if current.getnext() is not None:
                if current.getnext().getprev() == current:
                    print(current.getdata(),end=' <--> ')
                else:
                    raise BrokenLinkException(msg='can not print linkedlist',method='pprint')
            else:
                print(current.getdata())
            current = current.getnext()

    def reverse(self):

        if self.gethead() is None:
            raise HeadNodeException(method='reverse')

        current = self.gethead()
        while current.getnext() is not None:
            next_node = current.getnext()
            current.setprev(next_node)
            current = next_node
        self.sethead(current)

    def reversed(self) -> 'InitDoublyList':
        new_list = self.__class__()
        current = self.gethead()
        while current is not None:
            new_node = DoublyNode(current.getdata())
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

    @staticmethod
    def __create_from_collection(collection,_type:str) -> 'InitDoublyList':

        if not collection:
            raise ValueError('Collection Object '+_type+' is empty')

        linkedlist = InitDoublyList()
        for i in collection:
            node = DoublyNode(i)
            if linkedlist.gethead() is None:
                linkedlist.sethead(node)
                linkedlist.setsize(linkedlist.getsize() + 1)
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




























    