from functools import reduce,partial

def identity(x):
    """Return the input itself."""
    return x

def constant(c):
    """Return an function which always
    returns the input constant c."""
    def const_function(const,*args):
        return const
    return partial(const_function,c)

def add(*args):
    """Return the sum of the input."""
    def add2(x,y): return x + y
    return reduce(add2,args)

def mapv(f,*lst):
    """Return a vector of the result of map."""
    return list(map(f,*lst))

def vector(*args):
    """Return a vector of input parameters."""
    return args

def sequence(n,f = constant(0)):
    """Return a vector of length n, and initialize the i'th
    item with f(i).By default the vector will initialized with 0."""
    return [f(i) for i in range(0,n)]

def matrix(n,m,f = constant(0)):
    """Return a 2-dim vector which contains n vectors with length m.
    The j's item of vector i will be initialized by f(i,j).By default,
    the vector will be initialized with 0."""
    return [[f(i,j) for j in range(0,m)] for i in range(0,n)]

def flat(v):
    """Return a flat vector which contains the elements of v in their
    origin order.If the input is not a vector, return a vector which
    only contains the input."""
    if not isinstance(v,list): return [v]
    if not v: return []
    return reduce(add,mapv(flat,v))

def partition(v,f = identity):
    """Partition vector v by f(v[i]).
    e.g. partition([1,2,3,1,2,3],identity()) == {1:[1,1,1], 2:[2,2], 3:[3]}
    By default, the vector will be partitioned by identity function."""
    result = {}
    for item in v:
        key = f(item)
        s = result.get(key)
        if s:
            s.append(item)
        else:
            result.update({key:[item]})
    return result
