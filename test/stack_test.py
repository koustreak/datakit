import unittest
from datakit import stack
from datakit.util.exception import stack


class Teststack(unittest.TestCase):

    def test_stack_object(self):
        stack_obj = stack.InitStack(10)
        self.assertIsInstance(stack_obj,stack.InitStack,msg='stack object not initialized')
        self.assertEqual(stack_obj.get_stack_size(),10,msg='stack size initialize test case failed')
        self.assertEqual(stack_obj.get_top(),-1,msg='stack top initialize test case failed')
        self.assertIsInstance(stack_obj.is_empty(),bool,msg='stack is_empty test case failed')
        self.assertIsInstance(stack_obj.is_full(), bool, msg='stack is_full test case failed')
        del stack_obj

    def test_stack_push(self):
        stack_obj = stack.InitStack(10)
        stack_obj.push(100)
        self.assertEqual(stack_obj.get_top(),0,msg='stack top increase on push-event test case failed')
        del stack_obj

    def test_stack_pop(self):
        stack_obj = stack.InitStack(10)
        stack_obj.push(100)
        stack_obj.push(200)
        self.assertEqual(stack_obj.get_top(), 1, msg='stack top increase on push-event test case failed')
        stack_obj.pop()
        self.assertEqual(stack_obj.get_top(), 0, msg='stack top increase on pop-event test case failed')
        del stack_obj

    def test_validation_method(self):
        with self.assertRaises(stack_exceptions.StackInitError, msg='Validation Method test case failed'):
            stack.InitStack(-10)
        with self.assertRaises(stack_exceptions.StackInitError, msg='Validation Method test case failed'):
            stack.InitStack('stacksize=100')

    def test_stack_overflow(self):
        stack_obj = stack.InitStack(5)
        stack_obj.push(100)
        stack_obj.push(200)
        stack_obj.push(300)
        stack_obj.push(400)
        stack_obj.push(500)
        with self.assertRaises(stack_exceptions.StackOverflow, msg='stack Overflow test case failed'):
            stack_obj.push(600)
        del stack_obj

    def test_stack_emptypop(self):
        stack_obj = stack.InitStack(10)
        with self.assertRaises(stack_exceptions.StackEmpty, msg='stackEmpty test case failed'):
            stack_obj.pop()

    def test_stack_size_increase(self):
        stack_obj = stack.InitStack(10)
        stack_obj.push(100)
        stack_obj.increase_size()
        self.assertEqual(stack_obj.get_stack_size(),20,msg='stack size increase test case failed')
        del stack_obj

    def test_stack_get_max_element(self):
        stack_obj = stack.InitStack(10)
        stack_obj.push(100)
        stack_obj.push('200')
        with self.assertRaises(Exception,msg='stack Max Element test case failed'):
            stack_obj.get_max()
        stack_obj.pop()
        stack_obj.push(200)
        self.assertEqual(stack_obj.get_max(),200,msg='stack Max Element test case failed')
        del stack_obj

    def test_stack_get_min_element(self):
        stack_obj = stack.InitStack(10)
        stack_obj.push(100)
        stack_obj.push('200')
        with self.assertRaises(Exception, msg='stack Min Element test case failed'):
            stack_obj.get_min()
        stack_obj.pop()
        stack_obj.push(200)
        self.assertEqual(stack_obj.get_min(), 100, msg='stack Min Element test case failed')
        del stack_obj

    def test_stack_get_avg_element(self):
        stack_obj = stack.InitStack(10)
        stack_obj.push(100)
        stack_obj.push('200')
        with self.assertRaises(Exception, msg='stack Average Element test case failed'):
            stack_obj.get_average()
        stack_obj.pop()
        stack_obj.push(200)
        self.assertEqual(stack_obj.get_average(), 150, msg='stack Average Element test case failed')
        del stack_obj

    def test_stack_top_value(self):
        stack_obj = stack.InitStack(10)
        stack_obj.push(100)
        stack_obj.push('200')
        self.assertEqual(stack_obj.get_top(), 1, msg='stack Top Value test case failed')
        stack_obj.pop()
        self.assertEqual(stack_obj.get_top(), 0, msg='stack Top Value test case failed')
        del stack_obj

    def test_stack_from_list(self):
        with self.assertRaises(ValueError, msg='stack init from list test case failed'):
            stack.InitStack.stack_from_list([])
        with self.assertRaises(ValueError, msg='stack init from list test case failed'):
            stack.InitStack.stack_from_tuple(tuple())
        with self.assertRaises(ValueError, msg='stack init from list test case failed'):
            stack.InitStack.stack_from_set(set())

        stack_obj_list = stack.InitStack.stack_from_list([1, 2, 3, 4, 'end'])
        self.assertEqual(stack_obj_list.get_stack_size(), 5, msg='stack init from list test case failed')
        self.assertEqual(stack_obj_list.get_top(), 4, msg='stack init from list test case failed')
        del stack_obj_list

        stack_obj_tuple = stack.InitStack.stack_from_tuple(tuple([1, 2, 3, 4, 'end']))
        self.assertEqual(stack_obj_tuple.get_stack_size(), 5, msg='stack init from list test case failed')
        self.assertEqual(stack_obj_tuple.get_top(), 4, msg='stack init from list test case failed')
        del stack_obj_tuple

        stack_obj_set = stack.InitStack.stack_from_set(set([1, 2, 3, 4, 'end']))
        self.assertEqual(stack_obj_set.get_stack_size(), 5, msg='stack init from list test case failed')
        self.assertEqual(stack_obj_set.get_top(), 4, msg='stack init from list test case failed')
        del stack_obj_set



if __name__ == '__main__':
    unittest.main()