# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 25-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure ADT Version
import math

from stack import init_stack
from exceptions import InvalidParameter, StackInitError
from exceptions import NoneInputError
from exceptions import StackDownsizeError
from fnd_messages import stack_texts
from typing import List
from exceptions import bcolors

def stack_resize(stack, resize_option, safe_mode=True) -> bool:

    """
    it increases or decreases the size of the stack
    if resize_option == '+' then it will double the size of the stack
    if resize_option == '-' then it will reduce the size of the stack by half
    Currently the stack implementation is with list, later it will be changed.
    :param: resize_option : whether you want to downsize or increase the size of a stack
    :param: safe_mode : if safe_mode is on then stack downsize can not take place if it results in data leak
    :return: bool
    """

    if resize_option not in ('+', '-'):
        raise InvalidParameter(stack_texts.stack_resize_option_error)

    if resize_option == '+':
        stack.increase_size()

    if resize_option == '-':

        current_stack_size = stack.get_stack_size()
        if current_stack_size//2<=stack.get_top() and safe_mode:
            raise StackDownsizeError()

        if current_stack_size//2>stack.get_top():
            stack.decrease_size()

    return True

def __push_pop(stack) -> List:

    """
    In order to access middle element of a stack
    In order to delete middle element of a stack
    find min-max-average of a stack
        we need a temporary stack to pop from first stack and push in temp
        then pop from temp and then push it into input stack object
    :param stack: Input stack object
    :return: None
    """


    try:

        element_list = []
        temp_stack = init_stack(stack.get_stack_size())
        cur_top = stack.get_top()

        while cur_top >=0:
            cur_element = stack.pop()
            element_list.append(cur_element)
            cur_top -= 1
            temp_stack.push(cur_element)

        cur_top = temp_stack.get_top()

        while cur_top >=0:
            stack.push(temp_stack.pop())
            cur_top -= 1

        del temp_stack

        return element_list

    except Exception as ex:
        raise Exception('Error while doing push pop step with a temporary stack object ',str(ex))


def get_max(stack) -> object:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        stack_elements = __push_pop(stack)
        max_element = None
        if stack_elements:
            max_element = max(stack_elements)
        else:
            print(bcolors.WARNING+"Warning: It Appears the stack is empty")
        return max_element

    except Exception as ex:
        raise Exception('Error while finding max in stack ',str(ex))

def get_min(stack) -> object:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        stack_elements = __push_pop(stack)
        min_element = None
        if stack_elements:
            min_element = min(stack_elements)
        else:
            print(bcolors.WARNING+"Warning: It Appears the stack is empty"+ bcolors.ENDC)
        return min_element

    except Exception as ex:
        raise Exception('Error while finding min in stack ',str(ex))


def print_stack(stack) -> None:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        stack_elements = __push_pop(stack)
        if stack_elements:
            print('\n'.join(stack_elements[::-1]))
        else:
            print(bcolors.WARNING + "Warning: It Appears the stack is empty"+ bcolors.ENDC)

    except Exception as ex:
        raise Exception('Error while printing the stack element ', str(ex))

def find_average(stack) -> object:

    """
    Find the average of all elements of stack ,
    Only applicable for number type element
    :param stack:
    :return: object
    """

    try:

        stack_elements = __push_pop(stack)
        avg_value = None
        if stack_elements:
            avg_value = sum(stack_elements)/stack.get_stack_size()
        else:
            print(bcolors.WARNING + "Warning: It Appears the stack is empty" + bcolors.ENDC)
        return avg_value

    except Exception as ex:
        raise Exception('Error while finding min in stack ', str(ex))

def stack_from_collections(input_collection) -> object:

    """
    Create stack from input list
    :param input_collection: it is a list of objects
    :raises: StackInitError
    :return: stack object
    """

    if not input_collection:
        raise NoneInputError()

    stack = init_stack(len(input_collection))
    for i in input_collection:
        stack.push(i)
        print('Element ',i,' inserted successfully in the stack')

    return stack

stack_from_list = stack_from_collections
stack_from_tuple = stack_from_collections
stack_from_set = stack_from_collections
