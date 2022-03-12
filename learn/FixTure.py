import unittest
def setUpModule():
    print("setUpModule")
def tearDownModule():
    print("tearDownModule")
class Test03(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Test03class start")
    @classmethod
    def tearDownClass(cls) -> None:
        print("Test03class finish")
    def setUp(self) -> None:
        print("setUp执行")
    def tearDown(self) -> None:
        print("tearDown执行")
    def test01(self):
        print("test01 run")
    def test02(self):
        print("test02 run")
class Test04(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Test04class start")
    @classmethod
    def tearDownClass(cls) -> None:
        print("Test04class finish")
    def setUp(self) -> None:
        print("setUp4执行")
    def tearDown(self) -> None:
        print("tearDown4执行")
    def test01(self):
        print("test01 4run")
    def test02(self):
        print("test02 4run")
