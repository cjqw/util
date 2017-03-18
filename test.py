#!env /usr/bin/python3

import unittest
from util import *
from random import *

def eqv(a,b):
    """To tell if two vectors contains the same item in the same place.
    The items in the vectors can be compared with !=."""
    if len(a) != len(b): return False
    for i in range(0,len(a)):
        if a[i] != b[i]: return False
    return True

class utilTestCase(unittest.TestCase):

    def setUp(self):
        """Initialize some vector"""
        self.zerov = [0 for i in range(0,10)]
        self.onev = [1 for i in range(0,10)]
        self.incv = [i for i in range(0,10)]
        self.randv = [random() for i in range(0,10)]
        self.x = random()

    def test_identity(self):
        # Test when the input is a double
        assert self.x == (identity())(self.x)
        # Test when the input is a vector
        assert eqv(self.randv,identity()(self.randv))

    def test_constant(self):
        # Test when input is a double
        f = constant(self.x)
        assert f('a') == self.x
        assert f('a',self.incv) == self.x
        # Test when the input is a vector
        f = constant(self.randv)
        assert eqv(self.randv,f('a'))
        assert eqv(self.randv,f())
        assert eqv(self.randv,f(1,2,3,4,5,6,7))



if __name__ == '__main__':
    unittest.main()
