#!env /usr/bin/python3

import unittest
from util import *
from random import *

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
        for i in range(0,len(self.randv)):
            assert self.randv[i] == (identity())(self.randv)[i]
        assert len(self.randv) == len(identity()(self.randv))

    def test_constant(self):
        # Test when input is a double
        f = constant(self.x)
        assert f('a') == self.x
        assert f('a',incv) == self.x

if __name__ == '__main__':
    unittest.main()
