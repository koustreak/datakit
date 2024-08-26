# Author : koushik dutta
# Emial : koushikdutta2024@outlook.com
# Date : 28-Aug-2024
# Version : 1.0 Major
# Purpose : stack data structure

class HeadNodeException(Exception):

    def __init__(self,msg):
        super().__init__('Head Node Exception ',msg)
        self.error_code = 'LINKEDLIST'

