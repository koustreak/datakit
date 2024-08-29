#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: StackExceptions
Description: This is the parent class of all exceptions for datakit related to Stack
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 22-Aug-2024
Version: 1.0.0
License: MIT License
Usage: Stack.py
Dependencies: None

Change History:
    - 22-Aug-2024: Initial Version of the script
"""


from datakit.exceptions.BaseException import BaseException

class StackOverflow(BaseException):

    def __init__(self, *args) -> None:
        super().__init__(code='STACK',message="Stack Overflow, Increase the size of the stack", \
                         context=None, *args)

class StackEmpty(BaseException):

    def __init__(self, *args) -> None:
        super().__init__(code='STACK', message="Stack is empty, Insert element First", \
                         context=None, *args)

class ValidationTypeError(BaseException):

    def __init__(self,msg,*args) -> None:
        super().__init__(code="STACK", message="Validation Type Error "+str(msg), \
                        context=None, *args)

class StackPushError(BaseException):

    def __init__(self,msg,*args) -> None:
        super().__init__(code="STACK",message="Error while inserting data into stack "+str(msg), \
                        context=None, *args)

class StackPopError(BaseException):

    def __init__(self,msg,*args) -> None:
        super().__init__(code="STACK",message="Error while retrieving data from stack "+str(msg), \
                        context=None, *args)

class TempStackError(BaseException):

    def __init__(self,msg,*args) -> None:
        super().__init__(code="STACK", message='Error while doing push pop step with a temporary stack object '+msg,
                         context=None, *args)

class StackDownsizeError(BaseException):

    def __init__(self,*args) -> None:
        super().__init__(code="STACK", message='Can not downsize the error, as it can result in data leak \n'
                         'if stack_downsize is forced then please disable safe_mode', context=None, *args)

class StackUpsizeError(BaseException):

    def __init__(self,*args) -> None:
        super().__init__(code="STACK", message='Error while increasing the size of stack ', context=None, *args)

class StackAverageError(BaseException):

    def __init__(self,msg,*args) -> None:
        super().__init__(code="STACK", message='To get average all element of the stack \
                        should be int or float type '+str(msg),context=None, *args)

class StackMinMaxError(BaseException):

    def __init__(self,msg,*args) -> None:
        super().__init__(code="STACK", message='Min Max can not be applied to a \
                        heterogeneous collection object ' + str(msg), context=None, *args)

class StackInitError(BaseException):

    def __init__(self,*args) -> None:
        super().__init__(code="STACK", message='Can not Initialize a stack from the None input ',
                         context=None, *args)






