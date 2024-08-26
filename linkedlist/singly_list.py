# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 26-Aug-2024
# Version : 1.0 Major
# Purpose : singly linked list ADT implementation

from datakit.exceptions import bcolors
from static import linked_list_texts

class singly_list(object):

    def __init__(self):
        self.__head = None
        self.__size = 0

    def getHead(self):
        return self.__head

    def getSize(self):
        return self.__size

    def setSize(self,size):
        self.__size = size

    def setHead(self, node):
        if self.getHead() is not None:
            print(bcolors.WARNING + linked_list_texts.assign_head_node_error + bcolors.ENDC)
        self.setHead(node)
        self.setSize(self.getSize()+1)

    def insert_at_end(self, node):
        if self.getHead() is None:
            self.setHead(node)
        else:
            current = self.getHead()
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(node)
        self.setSize(self.getSize()+1)

    def insert_at_start(self, node):
        if self.getHead() is None:
            self.setHead(node)
        else:
            self.getHead().setNext(node)
            self.setHead(node)
        self.setSize(self.getSize()+1)

    def insert_at_pos(self, pos, node):
        current = self.getHead()
        count = 0
        if pos == 0:
            self.setHead(node)
        elif pos > self.getSize()-1:
            print(bcolors.FAIL+'Failed to insert code as the position \
                is greater than current list size'+bcolors.ENDC)
        else:
            while count<pos:
                current = current.getNext()
                count += 1
            node.setNext(current.getNext())
            current.setNext(node)
