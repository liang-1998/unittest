# 原始测试方法，比较预期结果与实际结果
# 不知道运行了几条测试用例，哪些成功失败；多条用例不适用

# 导入文件login.py中的方法
from login import get_username, get_password

def test_login_username():  # 登录用户名

    # 预期结果：自己登陆的账号
    except_useranme = 'test01'
    # 实际结果：显示在页面上的账号
    actual_name = get_username()
    # 比较预期结果与实际结果
    assert except_useranme == actual_name

def test_login_password():   # 登录密码
    # 预期结果：自己登陆的密码
    except_password = 'test01'
    # 实际结果：显示在页面上的密码
    actual_password = get_password()
    # 比较预期结果与实际结果
    assert except_password == actual_password

test_login_username()
test_login_password()







