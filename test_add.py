
import unittest

# 实现加法的方法
def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
     """
     def test_add_01(self):  # 有代码冗余
         res1 = add(1, 1)
         self.assertEqual(2, res1)

     def test_add_02(self):
        res2 = add(1, 4)
        self.assertEqual(5, res2)

     def test_add_03(self):
         res3 = add(-1, 2)
         self.assertEqual(1, res3)
     """

     # 用列表循环进行比较
     def test_add(self):
         test_data = [(1, 1, 2), (1, 0, 1), (-1, 2, 1)]
         for x,y,except_value in test_data:
             result = add(x, y)
             self.assertEqual(result, except_value)




if __name__ == '__main__':
    unittest.main()



