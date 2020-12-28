
import unittest
from parameterized import parameterized

# 实现加法的方法
def add(x, y):
    return x + y

# 测试数据
test_data = [(1, 1, 2), (1, 0, 1), (-1, 2, 1), (1, 2, 3)]

class TestAdd(unittest.TestCase):

     """
     # 用列表循环进行比较,一条测试用例
     def test_add(self):
         test_data = [(1, 1, 2), (1, 0, 1), (-1, 2, 1)]
         for x,y,except_value in test_data:
             result = add(x, y)
             self.assertEqual(result, except_value)
     """

     # 数据参数化（数据驱动）,使用parameterized包中的expand()方法
     # 测试用例随数据增加而增加
     @parameterized.expand(test_data)
     def test_add(self, a, b, except_result):
         result = add(a, b)
         self.assertEqual(result, except_result)


if __name__ == '__main__':
    unittest.main()



