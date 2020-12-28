
import unittest
from login import get_username, get_password

# 使用TestCase类
class Testlogin(unittest.TestCase):   # 继承TestCase类中的方法
    def test_login_username(self):  # 登录用户名

        # 预期结果：自己登陆的账号
        except_useranme = 'test01'
        # 实际结果：显示在页面上的账号
        actual_name = get_username()
        # 比较预期结果与实际结果
        self.assertEqual(except_useranme, actual_name)   # assertEqual(a, b) 比较a b两个值是否相等
        # assert except_useranme == actual_name

    def test_login_password(self):  # 登录密码
        # 预期结果：自己登陆的密码
        except_password = 'test01'
        # 实际结果：显示在页面上的密码
        actual_password = get_password()
        # 比较预期结果与实际结果
        self.assertEqual(except_password, actual_password)
        # assert except_password == actual_password

# 启动单元模块测试（测试用例入口）
# unittest.main()

# 1、使用 TestSuite 类中的 addTest() 方法添加测试用例
"""

# 创建一个测试套件，即一组用例组合
suite = unittest.TestSuite()
# 添加一条测试用例
# suite.addTest(Testlogin('test_login_username'))
# suite.addTest(Testlogin('test_login_password'))

# 添加多条测试用例
lst = [Testlogin('test_login_username'), Testlogin('test_login_password')]
suite.addTests(lst)
"""

# 2、使用 TestLoader 类中的 discover( 当前路径 . ,文件名 test*.py ) 方法来添加测试用例（建议使用这个）
suite = unittest.TestLoader().discover('.', pattern='test*.py')

# TextTestRunner() 测试用例执行器
runner = unittest.TextTestRunner()
runner.run(suite)   # run()方法，运行测试套件suite




















