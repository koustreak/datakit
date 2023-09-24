# Name : exception
# Author : koushik dutta
# Date : 20-June-2023
# Version : 1.0 Major
# Purpose : stack data structure

import warnings

class stack(object):

    def __init__(self,size:int,safe_mode_decr=False,
                    safe_mode_incr=False,
                    size_increase_threshold=None,
                    size_decrease_threshold=None):

        '''

        :param size: size of the stack
        top : top pointer of the stack
        safe_mode : safe_mode parameter while resizing a stack
        safe_mode_threshold : % of gap which is
        :return: None
        '''

        self.size = size
        self.stk = [None]*size
        self.top = -1
        self.safe_mode_decr = safe_mode_decr
        self.safe_mode_incr = safe_mode_incr
        self.size_increase_threshold = size_increase_threshold
        self.size_decrease_threshold = size_decrease_threshold

        print('It is recommended to use safe mode while resizing a stack')

        self.__validation()

    def __validation(self):

        if type(self.size) != type(0):
            raise Exception('size parameter value can be integer only , as it is the size of the stack')

        if self.safe_mode_decr and (not self.size_decrease_threshold):
            raise Exception('if safe_mode is on for stack size decrease , then a size_decrease_threshold is also required')

        if self.safe_mode_decr and self.size_decrease_threshold:
            if not (type(self.size_decrease_threshold) == type(1.0) or type(self.size_decrease_threshold) == type(1)):
                raise Exception('stack size decrease threshold parameter value should be either float or integer type')

        if self.safe_mode_incr and (not self.size_increase_threshold):
            raise Exception('if safe_mode is on for decrease , then a size_decrease_threshold is also required')

        if self.safe_mode_incr and self.size_increase_threshold:
            if not (type(self.size_increase_threshold) == type(1.0) or type(self.size_increase_threshold) == type(1)):
                raise Exception('stack size increase threshold parameter value should be either float or integer type')

    def insert(self,element=None):

        '''
        inserting into stack
        :param element: the
        :return: boolean
        '''

        assert element!=None,"Please insert a not None element"
        if self.top == self.size-1:
            raise Exception('STACK OVERFLOW!! no space left , either resize the stack or remove element')

        self.top += 1
        self.stk[self.top] = element


    def pop(self):

        '''

        :return: an element from stack
        :raise: stack underflow exceptions
        '''

        if self.top == -1:
            raise Exception('STACK EMPTY!! no element in the stack')

        temp = self.stk[self.top]
        self.stk[self.top] = None
        self.top -=1

        return temp

    def stack_resize(self,resize_option):

        '''
        it increase the size of the stack
        :param: resize_option : whether you want to downsize or increase the size of a stack
        :return: bool
        '''

        if resize_option == '+':

            if self.safe_mode:
                if self.stk.count(None):
                    gaps = (self.stk.count(None)/self.size)*100
                    if gaps > self.size_increase_threshold:
                        print('The % of vacant place in the stack in more than the size_increase_threshold , '
                              'hence stack size increase operation is aborted '
                              )
                        return False
            try:
                self.stk = self.stk+[None]*self.size
                self.size +=self.size
                return True
            except Exception as ex:
                print('error while increasing the size of the stack '+str(ex))
                return False

        if resize_option == '-':
            if any(self.stk):
                warnings.warn('The stack is not empty , you might lose data if you downsize the stack')

            if self.stk.count(None):
                filled_spots = ((self.size-self.stk.count(None)) / self.size) * 100
                if filled_spots > self.size_decrease_threshold:
                    print('filled_up_spot in the stack is greater than size_decrease_threshold parameter , '
                          'downsizing is aborted')

            if self.size%2:
                self.size = self.size//2+1
            else:
                self.size = self.size//2


