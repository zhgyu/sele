import unittest

class Test02(unittest.TestCase):
    def test001(self):
        #判断是否为True或False
        flag = True
        self.assertTrue(flag)
        flag = False
        self.assertFalse(flag)
        #判断字符相等
        self.assertEqual("斑马","斑马线")
        #判断后边字符包含前边整个字符
        self.assertIn("hello","hello world")
        #判断是否是none
        condition = None
        self.assertIsNone(condition)
        self.assertIsNotNone(condition)

