import unittest
from V3.page.page_register import PageRegister
import time
import parameterized
#新建测试类
class TestRegister(unittest.TestCase):
    def setUp(self) -> None:    #初始化
        #获取登录页面对象
        self.paggRegister = PageRegister()
    def tearDown(self) -> None:    #结束方法
        time.sleep(2)
        self.paggRegister.driver.quit()        #关闭驱动对象
    #新建测试方法
    @parameterized.parameterized.expand([("xiongmao","123456","123456",""),("xiongmao","123456","123456","1262912010@qq.com")])
    def test_register(self,username,pwd,confirmpwd,email):
        self.paggRegister.page_register(username,pwd,confirmpwd,email)
        #获取登录后的信息
        expect_email = "邮箱不能为空！"
        expect_user = "该用户名已存在"
        msg_user = self.paggRegister.page_get_user_error()
        msg_email = self.paggRegister.page_get_email_error()
        if(msg_email):
            try:
                self.assertEqual(msg_email,expect_email)
                print(msg_email)
            except AssertionError:
                self.paggRegister.driver.get_screenshot_as_file("./{}_test_login_exmail_not_null_fail.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
        if(msg_user):
            try:
                self.assertEqual(msg_user,expect_user)
                print(msg_user)
            except AssertionError:
                self.paggRegister.driver.get_screenshot_as_file("./{}_test_login_username_unique_fail.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

