from V4 import page
from V4.base.base import Base
class PageRegister(Base):
    #点击注册链接
    def page_click_register_link(self):
        self.base_click(page.register_link)
    #输入用户名
    def page_input_username(self,username):
        self.base_input(page.register_username,username)
    #输入密码
    def page_input_password(self,pwd):
        self.base_input(page.register_password,pwd)
    #输入确认密码
    def page_input_confirm_password(self,confirmpwd):
        self.base_input(page.register_confirm_password,confirmpwd)
    #输入邮箱
    def page_input_email(self,email):
        self.base_input(page.register_email,email)
    #点击注册
    def page_click_register_button(self):
        self.base_click(page.register_button)
    #获取邮箱框提示信息
    def page_get_email_error(self):
        return self.base_get_text(page.register_email_error)
    #获取用户名框提示信息
    def page_get_user_error(self):
        return self.base_get_text(page.register_user_error)
    #截图
    def page_get_screenshot(self,pth=""):
        self.base_get_screen_shot(pth)
    def page_register(self,username,pwd,confirmpwd,email):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_input_confirm_password(confirmpwd)
        self.page_input_email(email)
        self.page_click_register_button()