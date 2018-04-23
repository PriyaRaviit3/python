https://docs.scipy.org/doc/numpy/reference/generated/numpy.not_equal.html


equal:

np.equal([0, 1, 3,3], np.arange(4))
Out[12]: array([ True,  True, False,  True])

np.equal([0, 1, 2,3], np.arange(4))
Out[13]: array([ True,  True,  True,  True])

np.equal([1, 2,3,4], np.arange(4))
Out[14]: array([False, False, False, False])

np.equal([1],np.arange(1))
Out[15]: array([False])

np.equal([1],np.ones(1))
Out[16]: array([ True])


not_equal:


np.not_equal([1],np.ones(1))
Out[17]: array([False])

np.not_equal([0,1,2,3],np.arange(4))
Out[18]: array([False, False, False, False])

np.not_equal([1,2,3,4],np.arange(4))
Out[20]: array([ True,  True,  True,  True])


greater_equal:


np.greater_equal([0,1,2,3,4],np.arange(5))
Out[23]: array([ True,  True,  True,  True,  True])


