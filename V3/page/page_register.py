"""
页面对象层
类名：使用大驼峰取名模块名称，去掉下划线
方法：根据需求将每个操作步骤封装为一个方法
    方法名page_xxx
"""
from selenium import webdriver
class PageRegister():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.31.83:8080/community/index")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    #点击注册链接
    def page_click_register_link(self):
        self.driver.find_element_by_link_text("注册").click()
    #输入用户名
    def page_input_username(self,username):
        self.driver.find_element_by_css_selector("#username").send_keys(username)
    #输入密码
    def page_input_pwd(self,pwd):
        self.driver.find_element_by_css_selector("#password").send_keys(pwd)
    #输入确认密码
    def page_input_confirm_pwd(self,confirmpwd):
        self.driver.find_element_by_css_selector("#confirm-password").send_keys(confirmpwd)
    #输入邮箱
    def page_input_email(self,email):
        self.driver.find_element_by_css_selector("#email").send_keys(email)
    #点击注册
    def page_click_reigester_button(self):
        self.driver.find_element_by_css_selector("button[class='btn btn-info text-white form-control']").click()
    #获取用户名错误提示信息
    def page_get_user_error(self):
        return self.driver.find_element_by_xpath("//form/div[1]/div/div").text
    #获取邮箱错误提示信息
    def page_get_email_error(self):
        return self.driver.find_element_by_xpath("//form/div[4]/div/div").text
    #组装登录方法
    def page_register(self,username,pwd,confirmpwd,emial):
        self.page_click_register_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_confirm_pwd(confirmpwd)
        self.page_input_email(emial)
        self.page_click_reigester_button()

