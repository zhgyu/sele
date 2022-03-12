import unittest

version=30
@unittest.skip("该测试类未完成")
class Test01(unittest.TestCase):
    def test001(self):
        print("test001")
    @unittest.skipIf(version>20,"版本大于20不测试")
    def test002(self):
        print("未完成")