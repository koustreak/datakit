import unittest
from datakit import Node
from datakit import SinglyList
from datakit import ListException

class TestStack(unittest.TestCase):

    def test_linkedlist_object(self):
        list_obj = SinglyList.InitSinglyList()
        self.assertEquals(list_obj.getsize(),0,msg='Linked List initialization failed')
        self.assertEquals(list_obj.gethead(), None, msg='Linked List initialization failed')

    def test_linkedlist_insert(self):
        list_obj = SinglyList.InitSinglyList()
        list_obj.insert_front(Node.SinglyNode(101))
        self.assertEquals(list_obj.getsize(),1,msg='Linked List insert test failed')
        self.assertEquals(list_obj.gethead().getdata(),101,msg='Linked List insert test failed')
        list_obj.insert_rear(Node.SinglyNode(102))
        self.assertEquals(list_obj.getsize(), 2, msg='Linked List insert test failed')
        self.assertEquals(list_obj.gethead().getdata(), 101, msg='Linked List insert test failed')
        list_obj.insert_middle(1,Node.SinglyNode(107))
        self.assertEquals(list_obj.getsize(), 3, msg='Linked List insert test failed')

    def test_linkedlist_delete(self):
        list_obj = SinglyList.InitSinglyList()
        list_obj.insert_front(Node.SinglyNode(101))
        list_obj.insert_front(Node.SinglyNode(102))
        list_obj.insert_front(Node.SinglyNode(103))
        list_obj.delete_front()
        self.assertEquals(list_obj.getsize(), 2, msg='Linked List delete test failed')
        self.assertEquals(list_obj.gethead().getdata(), 102, msg='Linked List delete test failed')
        list_obj.delete_rear()
        self.assertEquals(list_obj.getsize(), 2, msg='Linked List delete test failed')
        self.assertEquals(list_obj.gethead().getdata(), 102, msg='Linked List delete test failed')

if __name__ == '__main__':
    unittest.main()