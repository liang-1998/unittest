
import unittest
from login import get_username, get_password

# TestCase下的初始化和清除方法：
# setUp() 初始化，每次测试方法前执行
# setUpClass() 初始化，整个类前执行
# tearDown() 清空，每次测试方法后执行
# tearDownClass()   清空，整个类结束运行时执行

version = 2.0
# 使用TestCase类
class Testlogin(unittest.TestCase):
    # 类的初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass：执行用例之前调用一次")

    # 类的清空方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass:执行用例之后调用一次")

    # 初始化方法
    def setUp(self) -> None:
        print("setUp:每次执行测试用力前执行")

    # 清空方法
    def tearDown(self) -> None:
        print("tearDown:每次执行测试用力后执行")

    def test_login_username(self):  # 登录用户名
        # 预期结果：自己登陆的账号
        except_useranme = 'test01'
        # 实际结果：显示在页面上的账号
        actual_name = get_username()
        # 比较预期结果与实际结果
        self.assertEqual(except_useranme, actual_name)


    # 跳过测试用例，直接跳过@unittest.skip('代码未完成')
    # @unittest.skip('跳过此测试用例')

    # 条件判断跳过测试用例，条件为真，跳过
    @unittest.skipIf(version > 1.0, '不执行此用例')
    def test_login_password(self):  # 登录密码
        # 预期结果：自己登陆的密码
        except_password = 'test01'
        # 实际结果：显示在页面上的密码
        actual_password = get_password()
        # 比较预期结果与实际结果
        self.assertEqual(except_password, actual_password)


# 创建一个测试套件，即一组用例组合
suite = unittest.TestSuite()
# 添加一条测试用例
suite.addTest(Testlogin('test_login_username'))
suite.addTest(Testlogin('test_login_password'))

# TextTestRunner() 测试用例执行器
runner = unittest.TextTestRunner()
runner.run(suite)   # run()方法，运行测试套件suite




















