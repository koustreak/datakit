#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: ListException
Description: This is the parent class of all exceptions for datakit related to LinkedList
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 23-Aug-2024
Version: 1.0.0
License: MIT License
Usage: Stack.py
Dependencies: None

Change History:
    - 23-Aug-2024: Initial Version of the script
"""

from datakit.exceptions.BaseException import BaseException

class HeadNodeException(BaseException):

    def __init__(self,method,*args):
        super().__init__(code='LINKEDLIST',message='Head Node is None ',
                         method=method, *args)

class BrokenLinkException(BaseException):

    def __init__(self,msg,method,*args):
        super().__init__(code='LINKEDLIST', message='There is a broken link ' + str(msg),
                         method=method, *args)

class InvalidParameter(BaseException):

    def __init__(self,reason,param_name,param_value,method,*args):
        message = f' Parameter - {param_name} has invalid Value {param_value}, reason {reason}'
        super().__init__(code='LINKEDLIST', message=message,method=method, *args)
