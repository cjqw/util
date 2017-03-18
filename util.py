from functools import reduce,partial

def identity():
    """Return an lambda expression which returns the input
    itself."""
    return lambda x: x

def constant(c):
    """Return an function which always
    returns the input constant c"""
    def const_function(const,*args):
        return const
    return partial(const_function,c)

def add(x,y):
    """Return the sum of the input"""
    return x + y

def mapv(f,x):
    """Return a vector of the result of map"""
    return list(map(f,x))

def reducev(f,x):
    """Return a vector of the result of reduce"""
    return list(reduce(f,x))

def sequence(n,f = constant(0)):
    """Return a vector of length n, and initialize the i'th
    item with f(i).By default the vector will initialized with 0."""
    return [f(i) for i in range(0,n)]

def matrix(n,m,f):
    """Return a 2-dim vector which contains n vectors with length m.
    The j's item of vector i will be initialized by f(i,j).By default,
    the vector will be initialized with 0."""
    # How to set default f ???
    # Maybe I need to change the definition of constant
    # return sequence(n,lambda x: [sequence(m, partial(f,i))])
    return [[f(i,j) for j in range(0,m)] for i in range(0,n)]

def flat(v):
    """Return a flat vector which contains the elements of v in their origin order."""
    # how to implement vector? ?
