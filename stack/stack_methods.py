# Author : Koushik Dutta
# Email : koushikdutta2024@outlook.com
# Date : 25-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure ADT Version
import math

from stack import Init
from exceptions import InvalidParameter
from exceptions import StackDownsizeError
from fnd_messages import stack_texts

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

def find_max_min(stack) -> object:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        temp_stack = Init(stack.get_stack_size())
        cur_top = stack.get_top()
        max_element = -math.inf
        min_element = math.inf

        while cur_top >=0:
            cur_element = stack.pop()
            max_element = max(max_element, cur_element)
            min_element = min(min_element, cur_element)
            cur_top -= 1
            temp_stack.push(cur_element)

        cur_top = temp_stack.get_top()

        while cur_top >=0:
            stack.push(temp_stack.pop())
            cur_top -= 1

        del temp_stack
        return max_element,min_element

    except Exception as ex:
        print('Error while finding max in stack ',str(ex))
        return None


def print_stack(stack) -> None:

    """
    Find the maximum and minimum value in a stack
    :param stack: stack object
    :return: object
    """

    try:

        temp_stack = Init(stack.get_stack_size())
        cur_top = stack.get_top()

        while cur_top >= 0:
            cur_element = stack.pop()
            print(cur_element)
            cur_top -= 1
            temp_stack.push(cur_element)

        cur_top = temp_stack.get_top()

        while cur_top >= 0:
            stack.push(temp_stack.pop())
            cur_top -= 1

        del temp_stack

    except Exception as ex:
        print('Error while finding max in stack ', str(ex))
        return None



