# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 20-June-2023
# Version : 1.0 Major
# Purpose : stack data structure ADT Version

import warnings
from fnd_messages import stack_texts
from exceptions import StackOverflow
from exceptions import StackEmpty
from exceptions import ValidationTypeError

class Stack(object):

    def __init__(self, size: int, safe_mode: bool = False) -> None:

        """

        :param size: size of the stack
        :param safe_mode: if safe_mode is on then stack size reduction is done if there is no data-loss
        :return: None
        """

        Stack.__validation(size,safe_mode)
        self.__size = size
        self.__safe_mode = safe_mode

        self.__stack = [None] * size
        self.__top = -1

    @staticmethod
    def __validation(size, safe_mode):

        """

        This process checks if the size of the stack is of valid datatype.
        Size variable should be a
        :return: None
        :raise: Exception
        """

        if not isinstance(size, int):
            if size < 0:
                raise ValidationTypeError(stack_texts.stack_size_error_text)
        if size == 0:
            warnings.warn(stack_texts.stack_size_zero_warn)

        if not isinstance(safe_mode, bool):
            raise ValidationTypeError(stack_texts.stack_safe_mode_flag_error)

    def push(self, element=None) -> bool:

        """

        inserting into stack
        :param element: element to be inserted
        :return: boolean
        :raise: Exception
        """

        assert element is not None,stack_texts.push_element_is_none

        if self.__top == self.__size - 1:
            raise StackOverflow()

        try:
            self.__top += 1
            self.__stack[self.__top] = element
            return True
        except Exception as ex:
            print('Error while insert into stack ',str(ex))
            return False

    def pop(self) -> object:

        """

        :return: an element from stack
        :raise: stack_underflow exceptions
        """

        if self.__top == -1:
            raise StackEmpty()

        element_returned = None
        try:
            element_returned = self.__stack[self.__top]
            self.__stack[self.__top] = None
            self.__top -= 1
        except Exception as ex:
            print('Error while pop from stack ',str(ex))

        return element_returned

    def get_stack_size(self):

        """

        Returns the size of the stack
        :return: Integer value of the size of the stack
        """

        return self.__size

    def get_top(self):

        """

        Returns the top of the stack
        :return: Integer value of the top of the stack
        """

        return self.__top