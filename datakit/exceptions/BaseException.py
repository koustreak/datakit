#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: BaseException
Description: This is the parent class of all exceptions for datakit
Author: Koushik Dutta
Email: koushikdutta2024@outlook.com
Date: 27-Aug-2024
Version: 1.0
License: MIT License
Inheritance: ListException.py , StackException.py
Dependencies: None

Change History:
    - 27-Aug-2024: Initial Version of the script
"""

class BaseException(Exception):
    """
    Base Exception class ,
    Customized for datakit
    """
    def __init__(self, code, message, context=None, *args):
        # Initialize the base class with the message and any extra arguments
        BaseException.__validation(code)
        super().__init__(message, *args)

        # Store custom attributes
        self.message = message
        self.code = code
        self.context = context
        self.extra_info = args  # Store extra positional arguments

    @staticmethod
    def __validation(code) -> None:
        if code is None:
            raise Exception('ErrorCode can not be None')
        if code not in ['STACK','LINKEDLIST']:
            raise Exception('ErrorCode can only be STACK or LINKEDLIST')

    def __str__(self) -> None:
        # Generate a string representation of the exception
        base_message = super().__str__()
        base_message += f" (Error Code: {self.code})"
        if self.context is not None:
            base_message += f" [Context: {self.context}]"
        if self.extra_info:
            base_message += f" [Extra Info: {', '.join(map(str, self.extra_info))}]"
        return base_message

    def get_extra_info(self):
        # Method to return extra information
        return self.extra_info