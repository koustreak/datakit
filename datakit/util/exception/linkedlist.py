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

class HeadNodeException(DataKitException):

    def __init__(self,message:str) -> None:
        super().__init__(message=message)

class BrokenLinkException(DataKitException):

    def __init__(self,message:str) -> None:
        super().__init__(message='There is a broken link ' + str(message))

class InvalidParameter(DataKitException):

    def __init__(self,param_name:str,param_value:str,exception_message:str) -> None:
        message = f' Parameter - {param_name} has invalid Value {param_value} '+exception_message
        super().__init__(message=message)
