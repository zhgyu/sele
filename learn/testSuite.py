import unittest
from test.test01 import Test01
from test.test02 import Test02

suite = unittest.TestSuite()
#addTest 类名(“方法名”)
suite.addTest(Test01("test01_02"))
suite.addTest(Test02("test02_01"))
suite.addTest(Test02("test02_02"))
suite.addTest(Test01("test01_03"))
#扩展测试套件 添加测试类中所有test开头的方法
# suite.addTest(Test01("test01_02"))
# suite.addTest(unittest.makeSuite(Test02))
# suite.addTest(Test01("test01_03"))
runner = unittest.TextTestRunner()
runner.run(suite)