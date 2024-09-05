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
from datakit.exceptions.ListException import HeadNodeException
from datakit.linkedlist.Node import SinglyNode

class CircularLinkedList(object):

    def __init__(self):
        self.__head:SinglyNode = None
        self.__length:int = 0

    def sethead(self,node:SinglyNode) -> bool:
        self.__head = node
        return True

    def gethead(self) -> SinglyNode:
        return self.__head

    def setsize(self,length) -> bool:
        self.__length = self.__length + length
        return True

    def getsize(self) -> int:
        return self.__length

    def pprint(self):
        if self.gethead() is None:
            raise HeadNodeException(method='pprint')
        currentnode = self.gethead()
        while currentnode.getnext()!=self.gethead():
            if currentnode.getnext()!=self.gethead():
                print(currentnode.getdata(),end=' --> ')
            else:
                print(currentnode.getdata())
            currentnode = currentnode.getnext()























