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
Inheritance: ListException.py , StackException.py
Dependencies: None

Change History:
    - 27-Aug-2024: Initial Version of the script
"""
from sympy.physics.units import current

from datakit.exceptions.ConsolePrint import bcolors
from datakit.linkedlist.Node import DoublyNode
from datakit.exceptions.ListException import InvalidParameter

class DoublyLinkedList(object):

    def __init__(self):

        self.__head = None
        self.__data = None
        self.__next_node = None
        self.__prev_node = None
        self.__size = 0

    def setHead(self, head:DoublyNode) -> bool:

        if self.getHead() is not None:
            print(bcolors.WARNING + 'Head Node is not None' + bcolors.ENDC)
        else:
            self.setSize(self.getSize() + 1)
        self.__head = head
        return True

    def getHead(self) -> DoublyNode:
        return self.__head

    def setSize(self, size: int) -> bool:
        self.__size = size

    def getSize(self) -> int:
        return self.__size

    def insert_at_start(self, node:DoublyNode) -> bool:
        if self.getHead() is None:
            self.setHead(node)
        else:
            current_head = self.getHead()
            current_head.setPrev(node)
            node.setNext(current_head)
            self.setHead(node)
        return True

    def insert_at_end(self, node:DoublyNode) -> bool:
        if self.getHead() is None:
            print(bcolors.WARNING + 'As Head is None , the input node will be set as head node ' + bcolors.ENDC)
            self.setHead(node)
        else:
            current = self.getHead()
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(node)
            node.setPrev(current)
        self.setSize(self.getSize() + 1)
        return True

    def insert_at_middle(self,pos:int, node:DoublyNode) -> bool:
        if self.getHead() is None:
            print(bcolors.WARNING + 'As Head is None , the input node will be set as head node ' + bcolors.ENDC)
            self.setHead(node)
        else:
            if pos > self.getSize() - 1:
                raise InvalidParameter('Failed to insert node as the position ' + str(pos) + ' \
                                is greater than current list size, to insert node at the end use insert_at_end')
            else:
                current = self.getHead()
                count = 0
                while count<pos:
                    current = current.getNext()
                    count += 1