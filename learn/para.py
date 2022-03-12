import unittest
from parameterized import parameterized
def add(x,y):
   return x+y;

class Test01(unittest.TestCase):
    #单个参数：值为列表
    @parameterized.expand(["1","2","3"])
    def test001(self,num):
        print("num:",num)
    #多个参数：值为列表嵌套元组
    @parameterized.expand([(1,2,3),(2,4,6),(3,5,8)])
    def test002(self,a,b,c):
        assert add(a,b)==c
        print("{}+{}={}".format(a,b,c))

    # data=[(1,2,3),(2,4,6),(3,5,8)]
    # @parameterized.expand(data)
    # def test002(self, a, b, c):
    #     print("{}+{}={}".format(a, b, c))
    #     assert a + b == c
    #
    # def get_data(self):
    #     return [(1,2,3),(2,4,6),(3,5,8)]
    #
    # @parameterized.expand(get_data())
    # def test002(self, a, b, c):
    #     print("{}+{}={}".format(a, b, c))
    #     assert a + b == c