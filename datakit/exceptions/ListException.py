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

    def __init__(self,msg='',*args):
        super().__init__(code='LINKEDLIST',message='Head Node is None '+str(msg),
                         context=None, *args)

class NoneNodeException(BaseException):

    def __init__(self,msg,*args):
        super().__init__(code='LINKEDLIST', message='Node Object is None ' + str(msg),
                         context=None, *args)

class InvalidParameter(BaseException):

    def __init__(self, msg, parameter, *args):
        super().__init__(code='LINKEDLIST', message='Parameter ' + str(parameter) + ' has None ' + str(msg),
                         context=None, *args)

