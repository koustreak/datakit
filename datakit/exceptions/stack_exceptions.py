# Author : koushik dutta
# Date : 15-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure

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

class StackAverageError(Exception):

    def __init__(self,msg) -> None:
        super().__init__('To get average all element of the stack should be int or float type ',msg)

class StackMinMaxError(Exception):

    def __init__(self,msg) -> None:
        super().__init__('Min Max can not be applied to a heterogeneous collection object ',msg)

class StackInitError(Exception):

    def __init__(self,obj_type,msg) -> None:
        super().__init__('Can not Initialize a stack from the None input ',obj_type,msg)






