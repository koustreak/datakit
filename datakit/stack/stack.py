#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Stack Implementation (ADT)
--------------------------
This module provides an implementation of the Stack Abstract Data Type (ADT),
supporting standard operations such as push, pop, peek, and is_empty.

Author: Koushik Dutta | koushikdutta2024@outlook.com
Created: 24-Aug-2024 | updated: 10-Mar-2025
Version: 1.0 | License: MIT License

Usage:
    from stack import Stack

Requirements:
    Python 3.x

Changelog:
    - 24-Aug-2024: Initial implementation
    - 10-Mar-2025: Change in exception
"""

from typing import List

from datakit.util.exception.stack import (
    StackInitError,
    StackOverflow,
    StackPushError,
    StackEmpty,
    StackPopError,
    StackStatisticsError
)
from datakit.util.logger import DataKitLogger

class InitStack(object):

    def __init__(self, size: int) -> None:

        self.__size = size
        self.__logger = DataKitLogger().get_logger()
        self.__validation()

        self.__stack = [None] * size
        self.__top = -1

    def __validation(self) -> None:

        if isinstance(self.__size, int):
            if self.__size < 0:
                raise StackInitError(message='The size parameter should be positive integer')

        if not isinstance(self.__size, int):
            raise StackInitError(message='The size parameter should be integer type')

        if self.__size == 0:
            self.__logger.warning('Size of stack is zero, still want to continue? ')

    def push(self, element=None) -> None:

        assert element is not None, 'Please insert a not None element'

        if self.__top == self.__size - 1:
            raise StackOverflow()

        try:
            self.__top += 1
            self.__stack[self.__top] = element
        except Exception as ex:
            raise StackPushError(message=str(ex))

    def pop(self) -> object:

        if self.__top == -1:
            raise StackEmpty()

        try:
            element_returned = self.__stack[self.__top]
            self.__stack[self.__top] = None
            self.__top -= 1
            return element_returned
        except Exception as ex:
            raise StackPopError(message=str(ex))

    def get_stack_size(self) -> int:

        return self.__size

    def get_top(self) -> int:

        return self.__top

    def is_empty(self) -> bool:

        return self.__top == -1

    def is_full(self) -> bool:

        return self.__top == self.__size-1

    def __del__(self) -> None:

        self.__logger.info("Stack Object is being deleted. Cleaning up...")
        self.__stack.clear()

    def spaces_left(self) -> int:

        return self.get_stack_size() - (self.get_top()+1)

    def __stack_elements(self) -> List:

        elements,i = [],0
        while i<=self.get_top():
            elements.append(self.__stack[i])
            i+=1
        return elements

    def get_max(self) -> object:

        try:
            elements = self.__stack_elements()
            if self.__top!=-1:
                return max(elements)
            else:
                self.__logger.warning("Warning: It Appears the stack is empty")
        except Exception as ex:
            raise StackStatisticsError(option='max',exception_msg=str(ex))

    def get_min(self) -> object:

        try:
            elements = self.__stack_elements()
            if self.__top!=-1:
                return min(elements)
            else:
                self.__logger.warning("Warning: It Appears the stack is empty")
        except Exception as ex:
            raise StackStatisticsError(option='min',exception_msg=str(ex))

    def get_average(self) -> object:

        try:
            elements = self.__stack_elements()
            if self.__top!=-1:
                cur_top = self.get_top() + 1
                cur_sum = sum(elements)
                return cur_sum / cur_top
            else:
                self.__logger.warning("Warning: It Appears the stack is empty")
        except Exception as ex:
            raise StackStatisticsError(option='avg',exception_msg=str(ex))

    def print_stack(self) -> None:

        try:
            if self.__top==-1:
                self.__logger.warning("Warning: It Appears the stack is empty")
            else:
                elements = self.__stack_elements()
                self.__logger.info('Printing Stack Elements.... Top Pointer is marked')
                max_width = max([len(str(i)) for i in elements])
                for i in range(len(elements)-1,-1,-1):
                    if i == len(elements)-1:
                        print('| '+ str(elements[i]).ljust(max_width+2,' ') +\
                              '| <-- TOP')
                    else:
                        print('| '+str(elements[i]).ljust(max_width+2,' ') +'|')
                    print('-'*(max_width+5))
        except Exception as ex:
            raise Exception('Error while printing the stack element ', str(ex))

    def reverse(self,in_place=False) -> object:

        if self.is_empty():
            raise StackEmpty()

        stack_elements = self.__stack_elements()
        if not in_place:
            temp_stack = self.__class__(size=self.get_stack_size())
            for i in stack_elements:
                temp_stack.push(i)
            return temp_stack
        else:
            cur_top = self.get_top()
            while cur_top!=-1:
                self.pop()
            for i in stack_elements:
                self.push(i)

    @staticmethod
    def __stack_from_collections(input_collection,input_type) -> "InitStack":

        if not input_collection:
            raise ValueError('input_collection cannot be empty , collection_type='+str(input_type))
        else:
            stack_object = InitStack(len(input_collection))
            for i in input_collection:
                stack_object.push(i)

            print('Elements from the collection, inserted successfully in the stack')

            return stack_object

    @staticmethod
    def stack_from_list(input_list: List) -> "InitStack":

        if isinstance(input_list, list):
            stack_object = InitStack.__stack_from_collections(input_collection=input_list,input_type='list')
            return stack_object
        else:
            raise TypeError('Input collection must be a list type')

    @staticmethod
    def stack_from_tuple(input_tuple: tuple) -> "InitStack":

        if isinstance(input_tuple, tuple):
            stack_object = InitStack.__stack_from_collections(input_collection=input_tuple,input_type='tuple')
            return stack_object
        else:
            raise TypeError('Input collection must be a tuple type')

    @staticmethod
    def stack_from_set(input_set: set) -> "InitStack":

        if isinstance(input_set, set):
            stack_object = InitStack.__stack_from_collections(input_collection=input_set,input_type='set')
            return stack_object
        else:
            raise TypeError('Input collection must be a set type')





