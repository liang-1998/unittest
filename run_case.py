
import unittest
from HTMLTestRunner import HTMLTestRunner

# 一组测试用例
suite = unittest.TestLoader().discover('.', pattern='test*.py')

# 控制台显示测试结果
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 使用HTMLTestRunner生成测试报告
# 1、定义生成测试报告的文件
test_report = 'test_report.html'
# 2、以写的模式打开上面的文件，将运行的结果写到文件中
with open(test_report, 'wb') as f:   # wb：以二进制格式打开一个文件只用于写入
    # 创建一个HTMLTestRunner的运行器，浏览器显示测试结果
    runner = HTMLTestRunner(f, title='测试报告', description='当前版本：v1.0')
    runner.run(suite)




