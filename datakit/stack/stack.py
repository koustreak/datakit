# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 20-June-2024
# Version : 1.0 Major
# Purpose : stack data structure ADT Version

import warnings
from datakit.exceptions.stack_exceptions import StackOverflow
from datakit.exceptions.stack_exceptions import StackEmpty
from datakit.exceptions.stack_exceptions import ValidationTypeError
from datakit.exceptions.stack_exceptions import StackDownsizeError

class Init(object):

    def __init__(self, size: int, safe_mode: bool = True) -> None:

        """
        :param size: size of the stack
        :param safe_mode: if safe_mode is on then stack size reduction is done if there is no data-loss
        :return: None
        """

        Init.__validation(size, safe_mode)
        self.__size = size
        self.__safe_mode = safe_mode

        self.__stack = [None] * size
        self.__top = -1

        print(f"Stack Object created with ID: {id(self)}")

    @staticmethod
    def __validation(size, safe_mode) -> None:

        """
        This process checks if the size of the stack is of valid datatype.
        Size variable should be a
        :return: None
        :raise: Exception
        """

        if isinstance(size, int):
            if size < 0:
                raise ValidationTypeError('stack size parameter should be positive integer')

        if not isinstance(size, int):
            raise ValidationTypeError('stack size parameter should be integer type')

        if size == 0:
            warnings.warn('size of stack is zero, still want to continue? ')

        if not isinstance(safe_mode, bool):
            raise ValidationTypeError('safe_mode flag can only be True or False')

    def push(self, element=None) -> None:

        """
        inserting into stack
        :param element: element to be inserted
        :return: boolean
        :raise: Exception
        """

        assert element is not None, 'Please insert a not None element'

        if self.__top == self.__size - 1:
            raise StackOverflow()

        try:
            self.__top += 1
            self.__stack[self.__top] = element
        except Exception as ex:
            raise Exception('Error while push into stack ',str(ex))

    def pop(self) -> object:

        """
        :return: an element from stack
        :raise: stack_underflow exceptions
        """

        if self.__top == -1:
            raise StackEmpty()

        try:
            element_returned = self.__stack[self.__top]
            self.__stack[self.__top] = None
            self.__top -= 1
            return element_returned
        except Exception as ex:
            raise Exception('Error while pop from stack ',str(ex))

    def get_stack_size(self) -> int:

        """
        Returns the size of the stack
        :return: Integer value of the size of the stack
        """

        return self.__size

    def get_top(self) -> int:

        """
        Returns the top of the stack
        :return: Integer value of the top of the stack
        """

        return self.__top

    def increase_size(self) -> None:

        """
        increase the size of the stack
        :return: boolean
        """

        try:
            self.__stack = self.__stack.extend([None] * self.__size)
            self.__size += self.__size
        except Exception as ex:
            raise Exception('Error while increase size of stack ',str(ex))

    def __decrease_size(self) -> None:

        warnings.warn(
            "stack size decrease is deprecated, not supproted now, might cause data leak if used",
            DeprecationWarning,
            stacklevel=2
        )
        """
        decrease the size of the stack
        It is 
        :return: None
        :raises: Exception
        """

        current_stack_size = self.get_stack_size()
        current_top_pos = self.get_top()

        if current_stack_size // 2 <= current_top_pos and self.__safe_mode:
            raise StackDownsizeError()

        if current_stack_size // 2 > current_top_pos:
            try:
                self.__stack = self.__stack[:self.__size//2]
                self.__size -= self.__size//2
            except Exception as ex:
                raise Exception('Error while decrease size of stack ',str(ex))

    def is_empty(self) -> bool:

        """
        Check if the stack is empty
        :return: boolean
        """

        return self.__top == -1

    def is_full(self) -> bool:

        """
        Check if the stack is empty
        :return: boolean
        """

        return self.__top == self.__size-1

    def __del__(self):
        print(f"Stack Object deleted with ID: {id(self)}")
