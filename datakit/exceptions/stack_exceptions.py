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
Usage: stack.py
Dependencies: None

Change History:
    - 22-Aug-2024: Initial Version of the script
"""

from datakit.exceptions.base_exception import BaseException

class StackOverflow(BaseException):

    def __init__(self, method, *args) -> None:
        super().__init__(code='STACK',message="Stack Overflow, Increase the size of the stack", \
                         method=method, *args)

class StackEmpty(BaseException):

    def __init__(self, method, *args) -> None:
        super().__init__(code='STACK', message="Stack is empty, Insert element First", \
                         method=method, *args)

class StackInitError(BaseException):

    def __init__(self,msg,method,*args) -> None:
        super().__init__(code="STACK", message="Validation Failed while initialize the stack "+str(msg), \
                        method=method, *args)

class StackPushError(BaseException):

    def __init__(self,msg,method,*args) -> None:
        super().__init__(code="STACK",message="Error while inserting data into stack "+str(msg), \
                        method=method, *args)

class StackPopError(BaseException):

    def __init__(self,msg,method,*args) -> None:
        super().__init__(code="STACK",message="Error while retrieving data from stack "+str(msg), \
                        method=method, *args)

class StackResizeError(BaseException):

    def __init__(self,msg,method,resize_option,*args) -> None:
        if resize_option == '-':
            message = 'Can not downsize the stack, maybe the stack is empty or safe_mode is True '
        else:
            message = 'Error while increasing the size of the stack '
        super().__init__(code="STACK", message=message+str(msg), method=method, *args)

class StackStatisticsError(BaseException):

    def __init__(self,msg,method,option,*args) -> None:
        if option in ('max','min'):
            message = 'To get min or max , the stack should be homogenous '
        if option == 'avg':
            message = 'To get average all element of the stack should be int or float type '
        super().__init__(code="STACK", message=message+str(msg),method=method, *args)




