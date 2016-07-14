#!/usr/bin/env python3.5
# -*- coding: UTF-8 -*-
"""Greeter.

Usage:
  launcher.py  <src> 
  launcher.py -h | --help

Options:
  -h --help     Show this screen.
""" 
 
import scipy.misc
import numpy as np
import os.path
from docopt import docopt
arguments = docopt(__doc__)
SRC=arguments['<src>']
print('mkdir white_low')
print('mkdir white_high')

src=[n for n in open(SRC)]
for p in src:
    p=p.strip()
    r,n=os.path.split(p)
    i=scipy.misc.imread(p)
    try:
        w,h=i.shape[:2]
    except:
        continue
    #if w<1920 or h<1080 or w*10/h<4*10/3:
    target='white_low'
    #else:
    #    target='white_high'
    m=np.mean(i)
    m=m*100000000/256
    pt=os.path.join(target,'%08d_%s'%(m,n))
    print('mv "%s" "%s"'%(p,pt))



