import glob
import sys
def f(p):
    for n in glob.glob(p,recursive=True):
        print(n)
root=sys.argv[1]
f('%s/**/*.jpg'%root)
f('%s/**/*.png'%root)
