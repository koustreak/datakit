# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 26-Aug-2024
# Version : 1.0 Major
# Purpose : singly linked list ADT implementation


class singly_list(object):

    def __init__(self):
        self.__head = None
        self.__size = 0

    def getHead(self):
        return self.__head

    def getSize(self):
        return self.__size

    def setHead(self, node):
        self.__head = node