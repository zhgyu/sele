from  selenium.webdriver.common.by import By
"""
注册页面配置信息
"""
register_link = (By.LINK_TEXT,"注册")
register_username = (By.ID,"username")
register_password = (By.ID,"password")
register_confirm_password = (By.ID,"confirm-password")
register_email = (By.ID,"email")
register_button = (By.CSS_SELECTOR,"button[class='btn btn-info text-white form-control")
register_user_error = (By.XPATH,"//form/div[1]/div/div")
register_email_error = (By.XPATH,"//form/div[4]/div/div")