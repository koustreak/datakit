# Author : koushik dutta
# Date : 15-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure

from typing import *

class StackOverflow(Exception):

    def __init__(self) -> None:
        super().__init__("Stack Overflow, Increase the size of the stack")

class StackEmpty(Exception):

    def __init__(self) -> None:
        super().__init__("Stack is empty, Insert element First")

class ValidationTypeError(Exception):

    def __init__(self,msg) -> None:
        super().__init__("Validation Type Error ",msg)

class StackPushError(Exception):

    def __init__(self,msg) -> None:
        super().__init__("Error while inserting data into stack ",msg)

class StackPopError(Exception):

    def __init__(self,msg) -> None:
        super().__init__("Error while inserting data into stack ",msg)

class InvalidParameter(Exception):

    def __init__(self,msg) -> None:
        super().__init__(msg)

class StackDownsizeError(Exception):

    def __init__(self) -> None:
        super().__init__('Can not downsize the error, as it can result in data leak \n'
                         'if stack_downsize is forced then please disable safe_mode')



