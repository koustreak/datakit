import unittest
from datakit import SinglyList
from datakit import ListException

class TestStack(unittest.TestCase):

    def test_stack_object(self):
        list_obj = SinglyList.InitSinglyList()
        self.assertEquals(list_obj.getsize(),0,msg='Linked List initialization failed')
        self.assertEquals(list_obj.gethead(), None, msg='Linked List initialization failed')



if __name__ == '__main__':
    unittest.main()