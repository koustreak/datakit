# Author : koushik dutta
# Date : 20-June-2023
# Version : 1.0 Major
# Purpose : stack data structure ADT Version

def stack_resize(stack, resize_option) -> bool:
    """

    it increases or decreases the size of the stack
    if resize_option == '+' then it will double the size of the stack
    if resize_option == '-' then it will reduce the size of the stack by half
    Currently the stack implementation is with list, later it will be changed.
    :param: resize_option : whether you want to downsize or increase the size of a stack
    :return: bool
    """

    if resize_option not in ('+', '-'):
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
            if temp < self.top + 1:
                raise Exception('Because Safe Mode is on, stack downsize is aborted, because it will results in'
                                'data-loss')

        try:
            self.size = temp
            self.stack = self.stack[:self.size]
            return True
        except Exception as ex:
            raise ex