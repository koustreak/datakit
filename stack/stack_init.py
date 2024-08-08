# Author : koushik dutta
# Date : 20-June-2023
# Version : 1.0 Major
# Purpose : stack data structure

import warnings


class Stack(object):

    def __init__(self, size: int, safe_mode: bool = False):

        """

        :param size: size of the stack
        :param safe_mode: if safe_mode is on then stack size reduction is done if there is no data-loss
        :return: None
        """

        self.size = size
        self.safe_mode = safe_mode
        self.__validation()

        self.stack = [None] * size
        self.top = -1

    def __validation(self):

        """

        This process checks if the size of the stack is of valid datatype.
        Size variable should be a
        :return: None
        :raise: Exception
        """

        if not isinstance(self.size, int):
            if self.size < 0:
                raise Exception('size parameter value can be integer only and greater than equal to 0, as it is the '
                                'size of the stack')
        if self.size == 0:
            warnings.warn('Size of stack is zero, still want to continue? ')

        if not isinstance(self.safe_mode, bool):
            raise Exception('safe_mode flag can only be True or False')

    def insert(self, element=None):

        """

        inserting into stack
        :param element: element to be inserted
        :return: boolean
        :raise: Exception
        """

        assert element != None, "Please insert a not None element"
        if self.top == self.size - 1:
            raise Exception('STACK OVERFLOW!! no space left , either resize the stack or remove element')

        try:
            self.top += 1
            self.stack[self.top] = element
            return True
        except Exception as e:
            raise e

    def pop(self):

        """

        :return: an element from stack
        :raise: stack underflow exceptions
        """

        if self.top == -1:
            raise Exception('STACK EMPTY!! no element in the stack')

        try:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return temp
        except Exception as e:
            raise e

    def stack_resize(self, resize_option):

        """

        it increases or decreases the size of the stack
        if resize_option == '+' then it will double the size of the stack
        if resize_option == '-' then it will reduce the size of the stack by half
        Currently the stack implementation is with list, later it will be changed. 
        :param: resize_option : whether you want to downsize or increase the size of a stack
        :return: bool
        """

        if resize_option not in ('+','-'):
            raise Exception('Invalid resize_option, it should be either + or -')

        if resize_option == '+':

            try:
                self.stack = self.stack + [None] * self.size
                self.size += self.size
                return True
            except Exception as ex:
                raise ex

        if resize_option == '-':

            if self.size % 2:
                temp = self.size // 2 + 1
            else:
                temp = self.size // 2

            if self.safe_mode:
                if temp < self.top+1:
                    raise Exception('Because Safe Mode is on, stack downsize is aborted, because it will results in'
                                        'data-loss')

            try:
                self.size = temp
                self.stack = self.stack[:self.size]
                return True
            except Exception as ex:
                raise ex

    def get_stack_size(self):

        """

        Returns the size of the stack
        :return: Integer value of the size of the stack
        """

        return self.size

    def get_top(self):

        """

        Returns the top of the stack
        :return: Integer value of the top of the stack
        """

        return self.top

    def element_search(self, element):

        """

        :param element: Element to be searched in the stack
        :return: Boolean if the element is in the stack
        """

        return element in self.stack
