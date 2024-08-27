# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 25-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure ADT Version

from typing import List

from datakit.exceptions.ConsolePrint import bcolors
from datakit.exceptions.StackExceptions import StackInitError
from datakit.stack.stack import Init


def __push_pop(stack_obj) -> List:

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
        temp_stack = Init(stack_obj.get_stack_size())
        cur_top = stack_obj.get_top()

        while cur_top >=0:
            cur_element = stack_obj.pop()
            element_list.append(cur_element)
            cur_top -= 1
            temp_stack.push(cur_element)

        cur_top = temp_stack.get_top()

        while cur_top >=0:
            stack_obj.push(temp_stack.pop())
            cur_top -= 1

        del temp_stack

        return element_list

    except Exception as ex:
        raise Exception('Error while doing push pop step with a temporary stack object ',str(ex))


def get_max(stack_obj) -> object:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        stack_elements = __push_pop(stack_obj)
        max_element = None
        if stack_elements:
            max_element = max(stack_elements)
        else:
            print(bcolors.WARNING+"Warning: It Appears the stack is empty")
        return max_element

    except Exception as ex:
        raise Exception('Error while finding max in stack ',str(ex))

def get_min(stack_obj) -> object:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        stack_elements = __push_pop(stack_obj)
        min_element = None
        if stack_elements:
            min_element = min(stack_elements)
        else:
            print(bcolors.WARNING+"Warning: It Appears the stack is empty"+ bcolors.ENDC)
        return min_element

    except Exception as ex:
        raise Exception('Error while finding min in stack ',str(ex))


def print_stack(stack_obj) -> None:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        stack_elements = __push_pop(stack_obj)
        if stack_elements:
            print('\n'.join([str(i) for i in stack_elements[::-1]]))
        else:
            print(bcolors.WARNING + "Warning: It Appears the stack is empty"+ bcolors.ENDC)
            print([None]*stack_obj.get_stack_size())

    except Exception as ex:
        raise Exception('Error while printing the stack element ', str(ex))

def get_average(stack_obj) -> object:

    """
    Find the average of all elements of stack ,
    Only applicable for number type element
    :param stack:
    :return: object
    """

    try:

        stack_elements = __push_pop(stack_obj)
        avg_value = None
        if stack_elements:
            cur_top = stack_obj.get_top()+1
            cur_sum = sum(stack_elements)
            avg_value = cur_sum/cur_top
        else:
            print(bcolors.WARNING + "Warning: It Appears the stack is empty" + bcolors.ENDC)
        return avg_value

    except Exception as ex:
        raise Exception('Error while finding min in stack ', str(ex))

def __stack_from_collections(input_collection) -> object:

    """
    Create stack from input list
    :param input_collection: it is a list of objects
    :raises: StackInitError
    :return: stack object
    """

    if not input_collection:
        raise StackInitError()

    stack = Init(len(input_collection))
    for i in input_collection:
        stack.push(i)
        print('Element ',i,' inserted successfully in the stack')

    return stack

stack_from_list = __stack_from_collections
stack_from_tuple = __stack_from_collections
stack_from_set = __stack_from_collections
