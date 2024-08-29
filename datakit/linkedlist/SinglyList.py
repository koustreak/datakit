# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 26-Aug-2024
# Version : 0.1.0
# Purpose : singly linked list ADT implementation

from datakit.exceptions.ConsolePrint import bcolors
from datakit.exceptions.ListException import NoneNodeException
from datakit.exceptions.ListException import InvalidParameter
from datakit.linkedlist.Node import SinglyNode

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

    def getHead(self) -> SinglyNode:

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

    def setHead(self, node: SinglyNode) -> bool:

        """
        sets the head of the singly linked list
        :param node: node object to set the head
        :return: None
        """
        if self.getHead() is not None:
            print(bcolors.WARNING + 'Head Node is not None' + bcolors.ENDC)
        else:
            self.setSize(self.getSize() + 1)
        self.__head = node
        return True

    def insert_at_end(self, node: SinglyNode) -> bool:

        """
        inserts the node at the end of the singly linked list
        :param node: node object
        :return: None
        """
        if self.getHead() is None:
            print(bcolors.WARNING+'As Head is None , the input node will be set as head node '+bcolors.ENDC)
            self.setHead(node)
        else:
            current = self.getHead()
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(node)
        self.setSize(self.getSize() + 1)
        return True

    def insert_at_start(self, node: SinglyNode) -> bool:

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

    def insert_at_middle(self, pos: int, node: SinglyNode) -> bool:

        """
        inserts the node at the given position in the singly linked list
        :param pos: position where the node will be inserted
        :param node: node object
        :return: None
        """
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

    def update_node_value(self, prev_value, curr_value) -> bool:

        """
        updates the value of the given node where the node data matches prev_value
        :param prev_value: update the value of the node whose value is prev_value
        :param curr_value: update the value from prev_value to curr_value
        :return: bool
        :raises: NoneNodeException
        """

        if self.getHead() is None:
            raise NoneNodeException('Head Node is None , failed to update')
        current = self.getHead()
        update_count = 0
        while current is not None:
            if current.getData() == prev_value:
                current.setData(curr_value)
                update_count += 1
            else:
                current = current.getNext()
        if update_count:
            return True
        return False

    def delete_at_start(self) -> bool:

        """
        deletes the node at the start of the singly linked list
        :return: bool
        :raises: NoneNodeException
        """
        if self.getHead() is None:
            raise NoneNodeException('Can not delete node at the end of the singly linked list')
        else:
            self.setHead(self.getHead().getNext())
            self.setSize(self.getSize()-1)
            return True

    def delete_at_end(self) -> bool:

        """
        deletes the node at the end of the singly linked list
        :return: bool
        """
        if self.getHead() is None:
            raise NoneNodeException('Can not delete node at the end of the singly linked list')

        current = self.getHead()
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(None)
        self.setSize(self.getSize() - 1)
        return True

    def delete_at_pos(self, pos: int) -> bool:

        if self.getHead() is None:
            raise NoneNodeException('Can not delete node at the end of the singly linked list')

        current = self.getHead()
        count = 0
        if pos == 0:
            self.delete_at_start()
        else:
            if pos > self.getSize():
                raise InvalidParameter('Failed to insert node as the position \
                                is greater than current list size, to insert node at the end use insert_at_end')
            else:
                while count < pos:
                    current = current.getNext()
                    count += 1
                if current.getNext().getNext() is not None:
                    current.setNext(current.getNext().getNext())
                else:
                    current.setNext(None)
                self.setSize(self.getSize() - 1)
                return True
