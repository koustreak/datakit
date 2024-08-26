# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 26-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure ADT Version


class singly_node(object):

    """
    Create Singly Linked List Node
    The Node has the below features
        data
        next_node
    ADT - True
    """

    def __init__(self, data,next=None):
        self.__data = data
        self.__next = next

    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

    def __str__(self):
        return 'Node->'+str(self.__data)

    def hasNext(self):
        return self.__next is not None

    def hasData(self):
        return self.__data is not None


class doubly_node(object):

    """
    Create Singly Linked List Node
    The Node has the below features
        data
        next_node
    ADT - True
    The doubly linked list nodes have two pointers
        next_node pointer
        prev_node pointer
    """

    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

    def setPrev(self, prev):
        self.__prev = prev

    def getPrev(self):
        return self.__prev

    def __str__(self):
        return 'Node->'+str(self.__data)

    def hasNext(self):
        return self.__next is not None

    def hasPrev(self):
        return self.__prev is not None

    def hasData(self):
        return self.__data is not None