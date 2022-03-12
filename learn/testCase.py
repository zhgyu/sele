import unittest

def add(x,y):
    return x+y;

class Test01(unittest.TestCase):
    def test_add(self):
        result = add(1,1)
        print("1+1=:",result)
    def test_add1(self):
        result = add(-1,-1)
        print("-1-1=",result)