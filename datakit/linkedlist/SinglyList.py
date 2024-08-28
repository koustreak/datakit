# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 26-Aug-2024
# Version : 0.1.0
# Purpose : singly linked list ADT implementation
from sympy.physics.units import current

from datakit.exceptions.ConsolePrint import bcolors
from datakit.exceptions.ListException import NoneNodeException

class SinglyLinkedList(object):

    """
    Implementation of a singly linked list.
    A singly linked list is a linked list which has one pointer , which points to next node
    """
    def __init__(self) -> None:

        """
        Constructor of singly linked list class
        :object variable: __head -> head of singly linked list
        :object variable: __size -> size of singly linked list
        :return: None
        """
        self.__head = None
        self.__size = 0

    def getHead(self) -> object:

        """
        returns the head of the singly linked list
        :return: Object
        """
        return self.__head

    def getSize(self) -> int:

        """
        returns the size of the singly linked list
        :return: integer
        """
        return self.__size

    def setSize(self, size: int) -> None:

        """
        sets the size of the singly linked list
        :param size: this method is to set the size of the singly linked list
        :return: None
        """
        self.__size = size

    def setHead(self, node: object) -> None:

        """
        sets the head of the singly linked list
        :param node: node object to set the head
        :return: None
        """
        if self.getHead() is not None:
            print(bcolors.WARNING + 'Head Node is not None' + bcolors.ENDC)
        self.setHead(node)
        self.setSize(self.getSize() + 1)

    def insert_at_end(self, node: object) -> bool:

        """
        inserts the node at the end of the singly linked list
        :param node: node object
        :return: None
        """
        if self.getHead() is None:
            self.setHead(node)
        else:
            current = self.getHead()
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(node)
        self.setSize(self.getSize() + 1)
        return True

    def insert_at_start(self, node: object) -> bool:

        """
        inserts the node at the start of the singly linked list
        :param node: node object
        :return: None
        """
        # if head is none then its the matter of setHead
        if self.getHead() is None:
            self.setHead(node)
        else:
            # set the head next to the node
            # point the head pointer to the node object
            self.getHead().setNext(node)
            self.setHead(node)
        self.setSize(self.getSize() + 1)
        return True

    def insert_at_pos(self, pos: int, node: object) -> None:

        """
        inserts the node at the given position in the singly linked list
        :param pos: position where the node will be inserted
        :param node: node object
        :return: None
        """
        current = self.getHead()
        count = 0
        if pos == 0:
            self.insert_at_start(node)
        elif pos > self.getSize() - 1:
            print(bcolors.FAIL + 'Failed to insert node as the position \
                is greater than current list size, to insert node at the end use insert_at_end' + bcolors.ENDC)
            return False
        else:
            while count < pos:
                current = current.getNext()
                count += 1
            node.setNext(current.getNext())
            current.setNext(node)
        return True

    def update_node_value(self, prev_value, curr_value) -> bool:

        """
        updates the value of the given node
        :param prev_value: update the value of the node whose value is prev_value
        :param curr_value: update the value from prev_value to curr_value
        :return: bool
        :raises: NoneNodeException
        """

        if self.getHead() is None:
            raise NoneNodeException()
        current = self.getHead()
        while current is not None:
            if current.getData() == prev_value:
                current.setData(curr_value)
                return True
            else:
                current = current.getNext()
        return False

    def delete_at_start(self) -> bool:

        """
        deletes the node at the start of the singly linked list
        :return: bool
        :raises: NoneNodeException
        """
        if self.getHead() is None:
            raise NoneNodeException()
        else:
            self.setHead(self.getHead().getNext())
            return True

    def delete_at_end(self) -> bool:

        """
        deletes the node at the end of the singly linked list
        :return: bool
        """
        if self.getHead() is None:
            raise NoneNodeException('Can not delete node at the end of the singly linked list')
