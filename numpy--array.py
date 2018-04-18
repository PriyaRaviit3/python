 import numpy as np

x=np.array([[1,2,3],[4,5,6]])

print(x)
[[1 2 3]
 [4 5 6]]

np.ravel(x)
Out[5]: array([1, 2, 3, 4, 5, 6])

np.ravel(x,order='F')
Out[6]: array([1, 4, 2, 5, 3, 6])

np.ravel(x,order='C')
Out[7]: array([1, 2, 3, 4, 5, 6])

np.full((3,4),3)
Out[8]: 
array([[3, 3, 3, 3],
       [3, 3, 3, 3],
       [3, 3, 3, 3]])

np.full((3,4),1)
Out[9]: 
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])

np.eye(3)
Out[10]: 
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

x=np.random.random(3)

x
Out[12]: array([0.24807911, 0.89302493, 0.2842984 ])

x=np.random.random((3,4))

x
Out[14]: 
array([[0.70069043, 0.79704775, 0.93075044, 0.74139217],
       [0.8171396 , 0.3111746 , 0.52461736, 0.12715384],
       [0.20824779, 0.53120223, 0.79817386, 0.45462913]])

x=np.random.normal(9,3(3,3))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-508d427d66ef> in <module>()
----> 1 x=np.random.normal(9,3(3,3))

TypeError: 'int' object is not callable

x=np.random.normal(5,3(3,3))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-35a108a1ce15> in <module>()
----> 1 x=np.random.normal(5,3(3,3))

TypeError: 'int' object is not callable

x=np.random.random((2,3,4))

x
Out[18]: 
array([[[0.71630897, 0.09742268, 0.80703373, 0.9332591 ],
        [0.71123611, 0.651147  , 0.95459225, 0.8706448 ],
        [0.72595944, 0.81562321, 0.7209005 , 0.08925924]],

       [[0.30585438, 0.33399147, 0.50658969, 0.68215625],
        [0.89391105, 0.68283254, 0.5548924 , 0.59071007],
        [0.92523037, 0.36051537, 0.28147302, 0.13126595]]])

x=np.random.normal(5,2(2,2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-e43b6d6aa830> in <module>()
----> 1 x=np.random.normal(5,2(2,2))

TypeError: 'int' object is not callable

x=np.random.normal(5,2,(2,2))

x
Out[21]: 
array([[3.55682119, 6.93507221],
       [1.53020503, 3.76737221]])

x=np.arange(0,20,2)

x
Out[23]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

x=np.linspace(1,20,3)

x
Out[25]: array([ 1. , 10.5, 20. ])

x=np.linspace(1,2,0.5)
C:\Users\I18N\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: DeprecationWarning: object of type <class 'float'> cannot be safely interpreted as an integer.
  """Entry point for launching an IPython kernel.

x=np.linspace(1,2,3)

x
Out[28]: array([1. , 1.5, 2. ])

x=np.linspace(1,2,5)

x
Out[30]: array([1.  , 1.25, 1.5 , 1.75, 2.  ])

x=np.linspace(1,20,9)

x
Out[32]: 
array([ 1.   ,  3.375,  5.75 ,  8.125, 10.5  , 12.875, 15.25 , 17.625,
       20.   ])

x=np.linspace(1,2,5)

x
Out[34]: array([1.  , 1.25, 1.5 , 1.75, 2.  ])

x=np.linspace(1,2,7)

x
Out[36]: 
array([1.        , 1.16666667, 1.33333333, 1.5       , 1.66666667,
       1.83333333, 2.        ])

x=np.linspace(1,2,10)

x
Out[38]: 
array([1.        , 1.11111111, 1.22222222, 1.33333333, 1.44444444,
       1.55555556, 1.66666667, 1.77777778, 1.88888889, 2.        ])
