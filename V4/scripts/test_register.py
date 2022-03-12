import unittest
from V4.page.page_register import PageRegister
from parameterized.parameterized import parameterized
def get_data():
    return [("xiongmao","123456","123456",""),("xiongmao","123456","123456","1262912010@qq.com")]
class TestRegister(unittest.TestCase):
    register = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.register = PageRegister()       #实例化获取页面对象
        cls.register.page_click_register_link()#点击注册链接
    @classmethod
    def tearDownClass(cls) -> None:
        cls.register.driver.quit()#关闭浏览器驱动对象
    @parameterized.expand(get_data())
    def test_Register(self,username,pwd,confirmpwd,email):    #注册测试方法
        self.register.page_register(username,pwd,confirmpwd,email)   #调用注册方法
        #调用注册提示信息
        result_userinfo = self.register.page_get_user_error()
        result_emailinfo = self.register.page_get_email_error()
        if(result_userinfo):
            expect_userinfo = "该用户名已存在"
            try:
                self.assertEqual(result_userinfo,expect_userinfo)
                print("result_userinfo:",result_userinfo)
            except AssertionError:
                self.register.page_get_screenshot("userinfo")
        if(result_emailinfo):
            expect_emailinfo = "邮箱不能为空！"
            try:
                self.assertEqual(result_emailinfo,expect_emailinfo)
                print("result_emailinfo",result_emailinfo)
            except AssertionError:
                self.register.page_get_screenshot("emailinfo")
