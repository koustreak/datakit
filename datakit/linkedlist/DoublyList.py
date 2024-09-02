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

from datakit.exceptions.ConsolePrint import bcolors
from datakit.linkedlist.Node import DoublyNode
from datakit.exceptions.ListException import InvalidParameter,HeadNodeException

class DoublyLinkedList(object):

    def __init__(self):

        self.__head = None
        self.__size = 0

    def sethead(self, head:DoublyNode) -> bool:
        self.__head = head

    def gethead(self) -> DoublyNode:
        return self.__head

    def setsize(self, size: int) -> bool:
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

    def insert_at_middle(self,pos:int, node:DoublyNode) -> bool:
        if self.gethead() is None:
            raise HeadNodeException(method='insert_middle')

        if pos == 0 or pos == self.getsize() - 1:
            print(bcolors.WARNING + 'To insert at front or rear end of the linkedlist , '
                                    'please use insert_front and insert_rear ' + bcolors.ENDC)
            return False
        else:
            if pos > self.getsize() - 1 or pos < 0:
                reason = f'Out of Bound exception , valid range is 0 to {self.getsize() - 1}'
                raise InvalidParameter(reason, 'position', pos, method='insert_middle')
            if not (isinstance(pos, int)):
                raise TypeError('Invalid value of pos parameter , it must be an integer')
            current = self.gethead()
            count = 0
            while count < pos - 1:
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
            raise HeadNodeException(method='delete_middle+987')

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