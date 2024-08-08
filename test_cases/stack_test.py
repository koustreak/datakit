import stack
import unittest

class StackTest(unittest.TestCase):

    def test_stack_size(self):
        obj = stack.Stack(10)
        self.assertEquals(obj.get_stack_size(), 10)

    def test_stack_top(self):
        obj = stack.Stack(10)
        self.assertEquals(obj.top,-1)

    def test_stack_resize(self):
        obj = stack.Stack(10)
        obj.stack_resize('+')
        self.assertEquals(obj.get_stack_size(),20)
        obj.stack_resize('-')
        self.assertEquals(obj.get_stack_size(), 10)

    def test_stack_bad_value(self):
        self.assertRaises(Exception, stack.Stack(-10))
        self.assertRaises(Exception, stack.Stack(10,'true'))

if __name__ == '__main__':
    unittest.main()