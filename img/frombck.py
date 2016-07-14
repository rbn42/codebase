import os.path
l=os.listdir('./bck')
for n in l:
    print('convert "./bck/%s"   -resize 1920x1080  "./bck2/%s.png"'%(n,n))
