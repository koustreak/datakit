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

    def getHead(self) -> SinglyNode:

        return self.__head

    def getSize(self) -> int:

        return self.__size

    def setSize(self, size: int) -> None:

        self.__size = size

    def setHead(self, node: SinglyNode) -> bool:

        if self.getHead() is not None:
            print(bcolors.WARNING + 'Head Node is not None' + bcolors.ENDC)
        else:
            self.setSize(self.getSize() + 1)
        self.__head = node
        return True

    def insert_at_end(self, node: SinglyNode) -> bool:

        if self.getHead() is None:
            print(bcolors.WARNING+'As Head is None , please use insert_at_start '+bcolors.ENDC)
            return False
        else:
            current = self.getHead()
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(node)
            self.setSize(self.getSize() + 1)
            return True

    def insert_at_start(self, node: SinglyNode) -> bool:

        # if head is none then setHead() will be invoked
        if self.getHead() is None:
            self.setHead(node)
        else:
            # set the head next to the node
            # point the head pointer to the node object
            node.setNext(self.getHead())
            self.setHead(node)
        self.setSize(self.getSize() + 1)
        return True

    def insert_at_middle(self, pos: int, node: SinglyNode) -> bool:

        if pos == 0 or pos == self.getSize() - 1:
            print(bcolors.WARNING + 'To insert at start dne end of the linkedlist , '
                                    'please use insert_at_start and insert_at_end ' + bcolors.ENDC)
            return False
        else:
            if pos > self.getSize() - 1 or pos < 0 or (not isinstance(pos,int)):
                raise InvalidParameter('Failed to insert node as the position ' + str(pos) + ' \
                            because it is out of range or not an integer ')
            current = self.getHead()
            count = 0
            while count < pos:
                current = current.getNext()
                count += 1
                node.setNext(current.getNext())
                current.setNext(node)
            self.setSize(self.getSize() + 1)
            return True

    def update_value(self, prev_value, curr_value) -> bool:

        if self.getHead() is None:
            raise NoneNodeException('Head Node is None , failed to update')
        current = self.getHead()
        update_count = 0
        while current is not None:
            if current.getData() == prev_value:
                current.setData(curr_value)
                update_count += 1
            current = current.getNext()
        if update_count:
            return True
        return False

    def update_value_at_pos(self, position: int, curr_value) -> bool:

        if self.getHead() is None:
            raise NoneNodeException('Head Node is None , failed to update')

        if position > self.getSize() - 1 or position < 0 or (not isinstance(position, int)):
            raise InvalidParameter('Failed to update node as the position ' + str(position) + ' \
                        because it is out of range or not an integer ')

        current = self.getHead()
        pos_count = 0
        while current is not None:
            if position == pos_count:
                current.setData(curr_value)
                return True
            current = current.getNext()
            pos_count += 1
        return False

    def delete_at_start(self) -> bool:

        if self.getHead() is None:
            raise NoneNodeException('Can not delete node at the end of the singly linked list')
        else:
            self.setHead(self.getHead().getNext())
            self.setSize(self.getSize()-1)
            return True

    def delete_at_end(self) -> bool:

        if self.getHead() is None:
            raise NoneNodeException('Can not delete node at the end of the singly linked list')

        if self.getSize() == 1:
            self.delete_at_start()
        else:
            current = self.getHead()
            prev = self.getHead()
            while current.getNext() is not None:
                prev = current
                current = current.getNext()
            prev.setNext(None)
            self.setSize(self.getSize() - 1)
            return True

    def delete_at_pos(self, pos: int) -> bool:

        if self.getHead() is None:
            raise NoneNodeException('Can not delete node at the end of the singly linked list')

        if pos > self.getSize() - 1 or pos < 0 or (not isinstance(pos, int)):
            raise InvalidParameter(msg='Invalid value for parameter pos, either out of range or not an integer '
                                   , parameter='position')

        current = self.getHead()
        prev = self.getHead()
        count = 0
        if pos == 0:
            self.delete_at_start()
        elif pos == self.getSize() - 1:
            self.delete_at_end()
        else:
            while count != pos:
                prev = current
                current = current.getNext()
                count += 1
            prev.setNext(current.getNext())
            self.setSize(self.getSize() - 1)
        return True

    def print_list(self) -> None:

        if self.getHead() is None:
            raise HeadNodeException('Linked List is empty')

        current = self.getHead()
        while current is not None:
            if current.getNext() is not None:
                print(current.getData(),end='->')
            else:
                print(current.getData(),end='')
            current = current.getNext()

    def reverse(self,in_place=False) -> 'SinglyLinkedList':

        if self.getHead() is None:
            raise HeadNodeException('Can not reverse the singly linked list')

        if in_place:
            new_list = self.__class__()
            current = self.getHead()
            while current is not None:
                new_list.setHead(current)
                current = current.getNext()
            return new_list
        else:
            current = self.getHead()
            prev = None
            while current is not None:
                next_node = current.getNext()
                current.setNext(prev)
                prev = current
                current = next_node

    def __get_stat(self,choice) -> object:

        if self.getHead() is None:
            raise HeadNodeException('Can not generate average, min, max')

        current = self.getHead()
        elements = []

        while current is not None:
            elements.append(current.getData())
            current = current.getNext()
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

        if not collection:
            raise ValueError('Collection '+str(_type)+' is empty ', collection)

        linkedlist = SinglyLinkedList()
        for i in collection:
            node = SinglyNode(i)
            if linkedlist.getHead() is None:
                linkedlist.setHead(node)
            else:
                linkedlist.insert_at_end(node)
        return linkedlist

    @staticmethod
    def from_list(input_list: List) -> 'SinglyLinkedList':

        if not isinstance(input_list, list):
            raise TypeError('Input list must be of type list')
        return SinglyLinkedList.__create_linkedlist_from_collection(input_list,'list')

    @staticmethod
    def from_tuple(input_tuple: Tuple) -> 'SinglyLinkedList':

        if not isinstance(input_tuple, tuple):
            raise TypeError('Input list must be of type list')
        return SinglyLinkedList.__create_linkedlist_from_collection(input_tuple,'tuple')

    @staticmethod
    def from_set(input_set: Set) -> 'SinglyLinkedList':

        if not isinstance(input_set, set):
            raise TypeError('Input list must be of type set')
        return SinglyLinkedList.__create_linkedlist_from_collection(input_set,'set')







