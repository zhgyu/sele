import unittest
from V5.page.page_register import PageRegister
from parameterized.parameterized import parameterized
from V5.tools.read_json import read_json
from V5.base.get_driver import GetDriver
from V5.tools.get_log import get_logging
from V5.tools.get_logger import GetLogger
# log = get_logging()
logger = GetLogger().get_logger()
def get_data():
    datas = read_json("data.json")
    arrs=[]
    for data in datas.values():
        arrs.append((data["username"],data["pwd"],data["confirmpwd"],data["email"]))
    return arrs
def get_data1():
    from V5.tools.read_txt import read_txt
    datas = read_txt('data.txt')
    arrs=[]
    for data in datas:
        arrs.append(tuple(data.strip().split(",")))
    return arrs
class TestRegister(unittest.TestCase):
    register = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.register = PageRegister(cls.driver)       #实例化获取页面对象
        cls.register.page_click_register_link()# 点击注册链接
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver() # cls.register.driver.quit()#关闭浏览器驱动对象
    @parameterized.expand(get_data1())
    def test_Register(self,username,pwd,confirmpwd,email):    #注册测试方法
        self.register.page_register(username,pwd,confirmpwd,email)   #调用注册方法
        result_userinfo = self.register.page_get_user_error() #调用注册提示信息
        result_emailinfo = self.register.page_get_email_error()
        if(result_userinfo):
            expect_userinfo = "该用户名已存在！"
            try:
                self.assertEqual(result_userinfo,expect_userinfo)
                logger.info("该用户名已存在")
                # log.info("该用户名已存在")
                print("result_userinfo:",result_userinfo)
            except AssertionError:
                logger.error(AssertionError)
                # log.error(AssertionError)
                self.register.page_get_screenshot("userinfo")
        if(result_emailinfo):
            expect_emailinfo = "邮箱不能为空！"
            try:
                self.assertEqual(result_emailinfo,expect_emailinfo)
                logger.info("邮箱不能为空！")
                # log.info("邮箱不能为空！")
                print("result_emailinfo",result_emailinfo)
            except AssertionError:
                # log.error("邮箱不能为空！ 测试错误")
                logger.error(AssertionError)
                self.register.page_get_screenshot("emailinfo")
