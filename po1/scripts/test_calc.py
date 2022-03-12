import unittest
from po1.page.page_calc import PageCalc
from parameterized.parameterized import parameterized
from po1.base.get_driver import GetDriver
from po1.tools.read_json import read_json
def get_data():
    datas = read_json('calc.json')
    arrs=[]
    for data in datas.values():
        arrs.append((data['a'],data['b'],data['c']))
    return arrs
class TestCalc(unittest.TestCase):
    pagecalc=None
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pagecalc = PageCalc(cls.driver)
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()
    @parameterized.expand(get_data())
    def test_calc_add(self,a,b,c):
        self.pagecalc.page_clear()
        self.pagecalc.page_add_calc(a,b)
        result = self.pagecalc.page_get_result()
        try:
            self.assertEqual(result,str(c))
            print("test_calc_add:",result)
        except AssertionError:
            self.pagecalc.base_get_screen_shot("test_calc_add")