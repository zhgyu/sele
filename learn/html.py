import unittest
from learn.test01 import Test01
from learn.test02 import Test02
from learn.HwTestReport import HTMLTestReport
suite = unittest.TestSuite()
suite.addTest(Test01("test01_02"))
suite.addTest(unittest.makeSuite(Test02))
suite.addTest(Test01("test01_03"))
with open('test.html', 'wb') as report:
    runner = HTMLTestReport(stream=report,verbosity=2)
    runner.run(suite)