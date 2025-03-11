#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Datakit LinkedList Exception
----------------------------
Custom exception handling for linked lists in the Datakit library.

Author: Koushik Dutta | koushikdutta2024@outlook.com
Created: 13-Jan-2025 | Updated: 11-Mar-2025
Version: 1.0 | License: MIT

Requirements:
    Python 3.x

Changelog:
    - 11-Mar-2025: Initial implementation
"""

from datakit.util.exception import DataKitException

class StackOverflow(DataKitException):

    def __init__(self) -> None:
        super().__init__(message="Stack Overflow, Exception happened , pop before push")

class StackEmpty(DataKitException):

    def __init__(self) -> None:
        super().__init__(message="Stack is empty, Insert element First")

class StackInitError(DataKitException):

    def __init__(self,message:str) -> None:
        super().__init__(message="Validation Failed while initialize the stack "+str(message))

class StackPushError(DataKitException):

    def __init__(self,message:str) -> None:
        super().__init__(message="Error while inserting data into stack "+str(message))

class StackPopError(DataKitException):

    def __init__(self,message:str) -> None:
        super().__init__(message="Error while retrieving data from stack "+str(message))

class StackStatisticsError(DataKitException):

    def __init__(self,option:str,exception_msg:str) -> None:
        if option in ('max','min'):
            message = 'To get min or max , the stack should be homogenous '+str(exception_msg)
        elif option == 'avg':
            message = 'To get average all element of the stack should be int or float type '+str(exception_msg)
        else:
            message = str(exception_msg)
        super().__init__(message=message)




