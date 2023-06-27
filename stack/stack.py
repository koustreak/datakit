# Name : exception
# Author : koushik dutta
# Date : 20-June-2023
# Version : 1.0 Major
# Purpose : stack data structure

import warnings

class stack(object):

    def __init__(self,size:int,safe_mode=False,safe_mode_threshold=None):

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
        self.safe_mode = safe_mode
        self.size_increase_threshold = safe_mode_threshold

        print('It is recommended to use safe mode while resizing a stack')

        self.__validation()

    def __validation(self):

        if type(self.size) != type(0):
            raise Exception('size parameter value can be integer only , as it is the size of the stack')

        if self.safe_mode and (not self.safe_mode_threshold):
            raise Exception('if safe_mode is on , then a safe_mode_threshold is also required')

    def insert(self,element=None):

        '''
        inserting into stack
        :param element: the
        :return: boolean
        '''

        assert element!=None,"Please insert a not None element"
        if self.top == self.size-1:
            raise Exception('STACK OVERFLOW!! no space left , either resize the stack or remove element')

        self.stk[self.top+1] = element
        self.top +=1

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
        :return: None
        '''

        if resize_option == '+':

            if self.safe_mode:
                if self.stk.count(None):
                    gaps = (self.stk.count(None)/self.size)*100


            self.stk = self.stk+[None]*self.size
            self.size +=self.size

        if resize_option == '-':
            if any(self.stk):
                warnings.warn('The stack is not empty , you might lose data if you downsize the stack')

            if self.size%2:
                self.size = self.size//2+1
            else:
                self.size = self.size//2


