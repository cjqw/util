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

    def test_add(self):
        x,y = random(),random()
        assert x+y == add(x,y)
        # Test with multiple inputs
        x,y,z = 'ab','cd','ef'
        assert x+y+z == add(x,y,z)
        assert add(*self.onev) == len(self.onev)

    def test_mapv(self):
        assert eqv(self.randv,mapv(identity(),self.randv))
        lst = self.onev
        res = mapv(add,lst,lst)
        for item in res: assert item == 2
        assert len(res) == len(lst)

    def test_vector(self):
        assert eqv(vector(*self.randv),self.randv)
        assert eqv(vector(*self.onev),self.onev)
        assert eqv([1,2,3],vector(1,*[2,3]))
        assert self.x == vector(self.x)[0]

    def test_sequence(self):
        assert eqv(self.zerov,sequence(len(self.zerov)))
        assert eqv(self.incv,sequence(len(self.incv),identity()))
        f = lambda x : x * self.x
        assert eqv(mapv(f,self.incv),
                   sequence(len(self.incv),f))

    def test_matrix(self):
        mat = matrix(5,5,constant(self.x))
        for item in mat:
            assert eqv(item,sequence(5,constant(self.x)))
        mat = matrix(5,5,vector)
        for i in range(0,5):
            item = mat[i]
            assert eqv(item,sequence(5,partial(vector,i)))


if __name__ == '__main__':
    unittest.main()
