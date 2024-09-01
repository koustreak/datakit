#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: Stack
Description: This is the ADT implementation of the Stack class.
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 24-Aug-2024
Version: 1.0
License: MIT License
Usage: stack_demo.py, stack_test.py
Dependencies: None

Change History:
    - 24-Aug-2024: Initial Version of the script
"""

import warnings
from typing import List
from datakit.exceptions.StackExceptions import (
    StackEmpty,
    StackInitError,
    StackOverflow,
    StackPushError,
    StackPopError,
    StackResizeError,
    StackStatisticsError
)
from datakit.exceptions.ConsolePrint import bcolors

class InitStack(object):

    def __init__(self, size: int, safe_mode: bool = True) -> None:

        InitStack.__validation(size, safe_mode)
        self.__size = size
        self.__safe_mode = safe_mode

        self.__stack = [None] * size
        self.__top = -1

    @staticmethod
    def __validation(size, safe_mode) -> None:

        if isinstance(size, int):
            if size < 0:
                raise StackInitError(msg='The size parameter should be positive integer',method='__validation')

        if not isinstance(size, int):
            raise StackInitError(msg='The size parameter should be integer type',method='__validation')

        if size == 0:
            warnings.warn('size of stack is zero, still want to continue? ')

        if not isinstance(safe_mode, bool):
            raise StackInitError(msg='safe_mode flag can only be True or False',method='__validation')

    def push(self, element=None) -> None:

        assert element is not None, 'Please insert a not None element'

        if self.__top == self.__size - 1:
            raise StackOverflow()

        try:
            self.__top += 1
            self.__stack[self.__top] = element
        except Exception as ex:
            raise StackPushError(str(ex))

    def pop(self) -> object:

        if self.__top == -1:
            raise StackEmpty()

        try:
            element_returned = self.__stack[self.__top]
            self.__stack[self.__top] = None
            self.__top -= 1
            return element_returned
        except Exception as ex:
            raise StackPopError(str(ex))

    def get_stack_size(self) -> int:

        return self.__size

    def get_top(self) -> int:

        return self.__top

    def increase_size(self) -> None:

        try:
            self.__stack.extend([None] * self.__size)
            self.__size += self.__size
        except Exception as ex:
            raise StackUpsizeError(str(ex))

    def __decrease_size(self) -> None:

        warnings.warn(
            "stack size decrease is deprecated, not supproted now, might cause data leak if used",
            DeprecationWarning,
            stacklevel=2
        )

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

        return self.__top == -1

    def is_full(self) -> bool:

        return self.__top == self.__size-1

    def __del__(self):
        # print(f"Stack Object deleted : {self}")
        pass

    # End of STACK ADT Implementation
    # Stack Ops ,
    # All builtin methods of the stack class

    def spaces_left(self) -> int:

        return self.get_stack_size() - (self.get_top()+1)

    def __push_pop(self) -> List:

        try:

            element_list = []
            temp_stack = self.__class__(size=self.get_stack_size())
            cur_top = self.get_top()

            while cur_top >= 0:
                cur_element = self.pop()
                element_list.append(cur_element)
                cur_top -= 1
                temp_stack.push(cur_element)

            cur_top = temp_stack.get_top()

            while cur_top >= 0:
                self.push(temp_stack.pop())
                cur_top -= 1

            del temp_stack

            return element_list

        except Exception as ex:
            raise TempStackError(str(ex))

    def get_max(self) -> object:

        try:

            stack_elements = self.__push_pop()
            max_element = None
            if stack_elements:
                max_element = max(stack_elements)
            else:
                print(bcolors.WARNING + "Warning: It Appears the stack is empty"+ bcolors.ENDC)
            return max_element

        except Exception as ex:
            raise StackMinMaxError(str(ex))

    def get_min(self) -> object:

        try:

            stack_elements = self.__push_pop()
            min_element = None
            if stack_elements:
                min_element = min(stack_elements)
            else:
                print(bcolors.WARNING + "Warning: It Appears the stack is empty" + bcolors.ENDC)
            return min_element

        except Exception as ex:
            raise StackMinMaxError(str(ex))

    def print_stack(self) -> None:

        try:

            stack_elements = self.__push_pop()
            if not stack_elements:
                print(bcolors.WARNING + "Warning: It Appears the stack is empty" + bcolors.ENDC)
            else:
                print(bcolors.UNDERLINE+'Printing Stack Elements.... Top Pointer is marked in CYAN'+bcolors.ENDC)
                max_width = max([len(str(i)) for i in stack_elements])
                print('-'*(max_width+5))
                for i in range(len(stack_elements)):
                    if i == 0:
                        print(bcolors.OKCYAN +'| '+ str(stack_elements[i]).ljust(max_width+2,' ') +\
                              '| <-- TOP'+ bcolors.ENDC)
                    else:
                        print('| '+str(stack_elements[i]).ljust(max_width+2,' ') +'|')
                    print('-'*(max_width+5))
        except Exception as ex:
            raise Exception('Error while printing the stack element ', str(ex))

    def get_average(self) -> object:

        try:

            stack_elements = self.__push_pop()
            avg_value = None
            if stack_elements:
                cur_top = self.get_top() + 1
                cur_sum = sum(stack_elements)
                avg_value = cur_sum / cur_top
            else:
                print(bcolors.WARNING + "Warning: It Appears the stack is empty" + bcolors.ENDC)
            return avg_value

        except Exception as ex:
            raise StackAverageError(str(ex))


    def reverse(self,in_place=False) -> object:

        if self.is_empty():
            raise StackEmpty()

        stack_elements = self.__push_pop()
        if not in_place:
            temp_stack = self.__class__(size=self.get_stack_size())
            for i in stack_elements[::-1]:
                temp_stack.push(i)
            return temp_stack
        else:
            for i in stack_elements:
                self.push(i)

    @staticmethod
    def __stack_from_collections(input_collection) -> object:

        if not input_collection:
            raise StackInitError()

        stack_object = InitStack(len(input_collection))
        for i in input_collection:
            stack_object.push(i)
            print('Element ', i, ' inserted successfully in the stack')

        return stack_object

    @staticmethod
    def stack_from_list(input_list: List) -> object:

        if isinstance(input_list, list):
            stack_object = InitStack.__stack_from_collections(input_collection=input_list)
            return stack_object
        else:
            raise TypeError('Input list must be a list type')

    @staticmethod
    def stack_from_tuple(input_tuple: tuple) -> object:

        if isinstance(input_tuple, tuple):
            stack_object = InitStack.__stack_from_collections(input_collection=input_tuple)
            return stack_object
        else:
            raise TypeError('Input list must be a tuple type')

    @staticmethod
    def stack_from_set(input_set: set) -> object:

        if isinstance(input_set, set):
            stack_object = InitStack.__stack_from_collections(input_collection=input_set)
            return stack_object
        else:
            raise TypeError('Input list must be a set type')





