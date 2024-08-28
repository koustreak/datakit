# Author : koushik dutta
# Emial : koushikdutta2024@outlook.com
# Date : 28-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure

from datakit.exceptions.BaseException import BaseException

class HeadNodeException(BaseException):

    def __init__(self,msg,*args):
        super().__init__(code='LINKEDLIST',message='Head Node Exception '+str(msg), \
                         context=None, *args)

class NoneNodeException(BaseException):

    def __init__(self,msg,*args):
        super().__init__(code='LINKEDLIST', message='Node Object is None ' + str(msg), \
                         context=None, *args)


