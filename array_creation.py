#!/bin/sh

#  array_creation.py
#  
#
#  Created by Joseph Fuentes on 8/27/17.
#
import numpy as np
a = np.ones((4,4),dtype=np.int8)
a [3, 1] = 6
a [2, 3] = 2
print(a)

x=np.array([2,3,4,5,6],dtype=np.int8)
b= np.diag([2.,3.,4.,5.,6.],k=-1)
print(b)

#Tiling for array creation
c=np.array([[4, 3], [2, 1]])
d = np.tile(c, (2, 2))
print(d)

