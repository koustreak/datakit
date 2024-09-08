import unittest

from sympy.physics.units import current

from datakit import Node
from datakit import SinglyList
from datakit import ListException
from datakit.exceptions.ListException import InvalidParameter


class TestStack(unittest.TestCase):

    def test_linkedlist_object(self):
        list_obj = SinglyList.InitSinglyList()
        self.assertEquals(list_obj.getsize(),0,msg='Linked List initialization failed')
        self.assertEquals(list_obj.gethead(), None, msg='Linked List initialization failed')
        del list_obj

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
        del list_obj

    def test_linkedlist_delete(self):
        list_obj = SinglyList.InitSinglyList()
        list_obj.insert_front(Node.SinglyNode(101))
        list_obj.insert_front(Node.SinglyNode(102))
        list_obj.insert_front(Node.SinglyNode(103))
        list_obj.delete_front()
        self.assertEquals(list_obj.getsize(), 2, msg='Linked List delete test failed')
        self.assertEquals(list_obj.gethead().getdata(), 102, msg='Linked List delete test failed')
        list_obj.delete_rear()
        self.assertEquals(list_obj.getsize(), 1, msg='Linked List delete test failed')
        self.assertEquals(list_obj.gethead().getdata(), 102, msg='Linked List delete test failed')
        with self.assertRaises(ListException.InvalidParameter, msg='linked list delete middle test case failed'):
            list_obj.delete_middle(2)
        with self.assertRaises(TypeError, msg='linked list delete middle test case failed'):
            list_obj.delete_middle('2')
        list_obj.delete_middle(0)
        self.assertEquals(list_obj.getsize(), 0, msg='Linked List delete test failed')
        with self.assertRaises(ListException.HeadNodeException,msg='empty list print didnt raise any exception'):
            list_obj.pprint()
        del list_obj

    def test_linkedlist_update(self):
        list_obj = SinglyList.InitSinglyList()
        list_obj.insert_front(Node.SinglyNode(101))
        list_obj.insert_front(Node.SinglyNode(102))
        self.assertEqual(list_obj.is_empty(),False,msg='Linked List is_empty test case failed')
        list_obj.update_by_value(102,111)
        self.assertEqual(list_obj.gethead().getdata(),111,msg='Linked List update value test case failed')
        with self.assertRaises(TypeError, msg='linked list delete middle test case failed'):
            list_obj.update_by_pos('2',109)
        with self.assertRaises(InvalidParameter, msg='linked list delete middle test case failed'):
            list_obj.update_by_pos(3,109)
        self.assertEquals(list_obj.update_by_value(103,109),False,msg='Linked List update test case failed')

    def test_linkedlist_reverse(self):
        list_obj = SinglyList.InitSinglyList()
        list_obj.insert_front(Node.SinglyNode(101))
        list_obj.insert_front(Node.SinglyNode(102))
        list_obj.insert_front(Node.SinglyNode(103))
        current_node = list_obj.gethead()
        while current_node.getnext() is not None:
            current_node = current_node.getnext()
        reversed_list = list_obj.reversed()
        list_obj.reverse()
        self.assertEqual(reversed_list.gethead().getdata(),current_node.getdata(),
                         msg='Linked List reverse test case failed')
        self.assertEqual(list_obj.gethead(),current_node,msg='Linked List reverse test case failed')
        del list_obj
        del reversed_list

    def test_linkedlist_from_collection(self):
        with self.assertRaises(ValueError, msg='linked list from_list test case failed'):
            SinglyList.InitSinglyList.from_list([])
        with self.assertRaises(ValueError, msg='linked list from_tuple test case failed'):
            SinglyList.InitSinglyList.from_tuple(tuple())
        with self.assertRaises(ValueError, msg='linked list from_set test case failed'):
            SinglyList.InitSinglyList.from_set(set())
        with self.assertRaises(TypeError, msg='linked list from_list test case failed'):
            SinglyList.InitSinglyList.from_list(tuple(1,2,34))
        with self.assertRaises(TypeError, msg='linked list from_tuple test case failed'):
            SinglyList.InitSinglyList.from_tuple({1:2,3:4})
        with self.assertRaises(TypeError, msg='linked list from_set test case failed'):
            SinglyList.InitSinglyList.from_set([2,9])

    def test_linkedlist_stat(self):
        list_obj = SinglyList.InitSinglyList()
        list_obj.insert_front(Node.SinglyNode(100))
        list_obj.insert_front(Node.SinglyNode(200))
        list_obj.insert_front(Node.SinglyNode(300))
        self.assertEqual(list_obj.getmax(),300,msg='get_max test case failed')
        self.assertEqual(list_obj.getmin(), 100, msg='get_min test case failed')
        self.assertEqual(list_obj.getavg(), 200, msg='get_avg test case failed')

if __name__ == '__main__':
    unittest.main()