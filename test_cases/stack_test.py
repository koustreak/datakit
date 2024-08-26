import stack
import unittest


class StackTest(unittest.TestCase):

    def test_stack_size(self):
        obj = stack.Init(10)
        self.assertEquals(obj.get_stack_size(), 10)

    def test_stack_top(self):
        obj = stack.Init(10)
        self.assertEquals(obj.get_top(),-1)

    def test_method_return(self):
        obj = stack.Init(10)
        self.assertIsInstance(obj.is_empty(), bool)
        self.assertIsInstance(obj.is_full(), bool)
        self.assertIsInstance(obj.get_top(), int)
        self.assertIsInstance(obj.get_stack_size(), int)



if __name__ == '__main__':
    unittest.main()