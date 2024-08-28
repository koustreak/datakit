# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 26-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure ADT Version


class SinglyNode(object):

    """
    Create Singly Linked List Node
    The Node has the below features
        data
        next_node
    ADT - True
    The singly linked list has one pointer only
    """

    def __init__(self, data,next_node=None) -> None:

        """
        constructor of singly linked list node
        :param data: value of the node
        :param next_node: this is the pointer which will point to the next node
        """
        self.__data = data
        self.__next = next_node

    def setData(self, data) -> None:

        """
        setter of the data of the node
        :param data: value of the node
        :return: None
        """
        self.__data = data

    def getData(self) -> object:

        """
        getter of the data of the node
        :return: node value
        """
        return self.__data

    def setNext(self, next_node: object) -> None:

        """
        setter of the next node pointer .
        the next pointer actually stores a node object .
        :param next_node: node object to be saved as next node pointer
        :return: None
        """
        self.__next = next_node

    def getNext(self) -> object:

        """
        getter of the next node pointer .
        :return: node object , it can return None also
        """
        return self.__next

    def hasNext(self) -> bool:

        """
        check if the node's next pointer pointing to a node object
        :return: boolean
        """
        return self.__next is not None

    def hasData(self) -> bool:

        """
        check if the node has any data or not
        :return: boolean
        """
        return self.__data is not None


class DoublyNode(object):

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

    def __init__(self, data, prev=None, next_node=None) -> None:

        """
        constructor of doubly linked list node
        :param data: value of the node
        :param prev: this is the pointer which will point to the previous node
        :param next_node: this is the pointer which will point to the next node
        """
        self.__data = data
        self.__next = next_node
        self.__prev = prev

    def setData(self, data) -> None:

        """
        setter of the data of the node
        :param data: value of the node
        :return: None
        """
        self.__data = data

    def getData(self) -> object:

        """
        getter of the data of the node
        :return: data of the node
        """
        return self.__data

    def setNext(self, next_node: object) -> None:

        """
        setter of the next node pointer .
        :param next_node: node object to be saved as next node pointer
        :return: None
        """
        self.__next = next_node

    def getNext(self) -> object:

        """
        getter of the next node pointer .
        :return: object , it can return None also
        """
        return self.__next

    def setPrev(self, prev_node: object) -> None:

        """
        setter of the previous node pointer .
        :param prev_node: it is a node object which points to the previous node
        :return: None
        """
        self.__prev = prev_node

    def getPrev(self) -> object:

        """
        getter of the previous node pointer . It returns the previous node connected to the current node
        :return: node object , it can return None also
        """
        return self.__prev

    def hasNext(self) -> bool:

        """
        check if the node's next pointer pointing to a node object'
        :return: boolean
        """
        return self.__next is not None

    def hasPrev(self) -> bool:

        """
        check if the node's previous pointer pointing to a node object'
        :return: boolean
        """
        return self.__prev is not None

    def hasData(self) -> object:

        """
        check if the node has any data or not
        :return: node value
        """
        return self.__data is not None