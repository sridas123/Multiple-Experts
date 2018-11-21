# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:49:42 2018

@author: sxd170431
"""
import numpy as np
import matplotlib.pyplot as plt
sri=np.array([[1,2,3],[4,2,3],[1,3,4],[9,2,3]])
print sri
trajectory=[(1, ['bOn(s1,b1,t1)', 'bOn(s1,b2,t1)', 'tIn(s1,t1,c1)', 'bOn(s1,b3,t2)', 'bOn(s1,b4,t2)', 'tIn(s1,t2,c1)', 'bOn(s1,b5,t3)', 'bOn(s1,b6,t3)', 'bOn(s1,b7,t3)', 'bOn(s1,b8,t3)', 'bOn(s1,b9,t3)', 'bOn(s1,b10,t3)', 'tIn(s1,t3,c1)', 'move(s1,t2,c2)']), (2, ['bOn(s2,b1,t1)', 'bOn(s2,b2,t1)', 'tIn(s2,t1,c1)', 'bOn(s2,b5,t3)', 'bOn(s2,b6,t3)', 'bOn(s2,b7,t3)', 'bOn(s2,b8,t3)', 'bOn(s2,b9,t3)', 'bOn(s2,b10,t3)', 'tIn(s2,t3,c1)', 'bOn(s2,b3,t2)', 'bOn(s2,b4,t2)', 'tIn(s2,t2,c2)', 'unload(s2,b7,t3)']), (3, ['bOn(s3,b1,t1)', 'bOn(s3,b2,t1)', 'tIn(s3,t1,c1)', 'bOn(s3,b5,t3)', 'bOn(s3,b6,t3)', 'bOn(s3,b8,t3)', 'bOn(s3,b9,t3)', 'bOn(s3,b10,t3)', 'tIn(s3,t3,c1)', 'bIn(s3,b7,c1)', 'bOn(s3,b3,t2)', 'bOn(s3,b4,t2)', 'tIn(s3,t2,c2)', 'unload(s3,b6,t3)']), (4, ['bOn(s4,b1,t1)', 'bOn(s4,b2,t1)', 'tIn(s4,t1,c1)', 'bOn(s4,b5,t3)', 'bOn(s4,b8,t3)', 'bOn(s4,b9,t3)', 'bOn(s4,b10,t3)', 'tIn(s4,t3,c1)', 'bIn(s4,b7,c1)', 'bIn(s4,b6,c1)', 'bOn(s4,b3,t2)', 'bOn(s4,b4,t2)', 'tIn(s4,t2,c2)', 'unload(s4,b2,t1)']), (5, ['bOn(s5,b1,t1)', 'tIn(s5,t1,c1)', 'bOn(s5,b5,t3)', 'bOn(s5,b8,t3)', 'bOn(s5,b9,t3)', 'bOn(s5,b10,t3)', 'tIn(s5,t3,c1)', 'bIn(s5,b7,c1)', 'bIn(s5,b6,c1)', 'bIn(s5,b2,c1)', 'bOn(s5,b3,t2)', 'bOn(s5,b4,t2)', 'tIn(s5,t2,c2)', 'move(s5,t3,c3)']), (6, ['bOn(s6,b1,t1)', 'tIn(s6,t1,c1)', 'bIn(s6,b7,c1)', 'bIn(s6,b6,c1)', 'bIn(s6,b2,c1)', 'bOn(s6,b3,t2)', 'bOn(s6,b4,t2)', 'tIn(s6,t2,c2)', 'bOn(s6,b5,t3)', 'bOn(s6,b8,t3)', 'bOn(s6,b9,t3)', 'bOn(s6,b10,t3)', 'tIn(s6,t3,c3)', 'destination(s6,c3)', 'move(s6,t2,c2)']), (7, ['bOn(s7,b1,t1)', 'tIn(s7,t1,c1)', 'bIn(s7,b7,c1)', 'bIn(s7,b6,c1)', 'bIn(s7,b2,c1)', 'bOn(s7,b3,t2)', 'bOn(s7,b4,t2)', 'tIn(s7,t2,c2)', 'bOn(s7,b5,t3)', 'bOn(s7,b8,t3)', 'bOn(s7,b9,t3)', 'bOn(s7,b10,t3)', 'tIn(s7,t3,c3)', 'destination(s7,c3)', 'unload(s7,b8,t3)'])]
reversed_trajectory = trajectory[::-1]
print reversed_trajectory