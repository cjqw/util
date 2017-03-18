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

    def test_identity(self):
        # Test when the input is a double
        x = random()
        assert x == (identity())(x)
        # Test when the input is a vector
        for i in range(0,len(self.randv)):
            assert self.randv[i] == (identity())(self.randv)[i]
        assert len(self.randv) == len(identity()(self.randv))

if __name__ == '__main__':
    unittest.main()
