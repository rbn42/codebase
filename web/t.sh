#!/bin/bash 
mkdir /dev/shm/asdf
cd /dev/shm/asdf
rm *
export URL="http://tieba.baidu.com/mo/q---11D4E04E73333FF5048FBD76833B8BD7%3AFG%3D1--1-3-0--2--wapp_1467617510390_998/m?kw=linux&lp=5011&lm=&pn=0"
wget $URL --quiet
export URL="http://tieba.baidu.com/mo/q---11D4E04E73333FF5048FBD76833B8BD7%3AFG%3D1--1-3-0--2--wapp_1467617510390_998/m?kw=linux&lp=5011&lm=&pn=10"
wget $URL --quiet
export URL="http://tieba.baidu.com/mo/q---11D4E04E73333FF5048FBD76833B8BD7%3AFG%3D1--1-3-0--2--wapp_1467617510390_998/m?kw=linux&lp=5011&lm=&pn=20"
wget $URL --quiet
export URL="http://tieba.baidu.com/mo/q---11D4E04E73333FF5048FBD76833B8BD7%3AFG%3D1--1-3-0--2--wapp_1467617510390_998/m?kw=linux&lp=5011&lm=&pn=30"
wget $URL --quiet
export SCRIPT="""
import sys
import re
import os.path
from pyquery import PyQuery as pq
l=[]
for p in sys.argv[1:]:
    for i in re.findall('<a.+?</a>',open(p).read()):
        i=pq(i).text()
        if '桌面' in i:
            l.append(i)
            print(i)
cache='/dev/shm/jklasdfjsd_cache'
if not os.path.exists(cache):
    with open(cache,'w') as f:
        f.write('set()')
l=set(l)
o=eval(open(cache).read())
for i in l-o:
    os.system('notify-send %s'%i)
open(cache,'w').write(str(l))

"""
python -c "$SCRIPT" * 
