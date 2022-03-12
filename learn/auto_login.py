import unittest
import selenium.webdriver as webdriver
import time
class TestAutoLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.itspxx.com/member.php?mod=logging&action=login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()
    def test01(self):
        # time.sleep(2)
        self.driver.find_element_by_css_selector("input[name='username']").send_keys("admin")
        self.driver.find_element_by_css_selector("input[name='password']").send_keys("123456")
        self.driver.find_element_by_css_selector("input[name='seccodeverify']").send_keys()
        self.driver.find_element_by_css_selector("button[name='loginsubmit']").click()
        result=self.driver.find_element_by_css_selector("td[class='pc_c']>div[class='pc_inner']").text
        print(result)
        try:
            self.assertEqual(result,"抱歉，验证码填写错误!")
        except AssertionError:
            self.driver.get_screenshot_as_file("{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
            raise