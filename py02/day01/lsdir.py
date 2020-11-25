import os
import sys

def lsdir(fname):
    for path, folders, files in os.walk(fname):
        print('%s:' % path)
        for i in folders:
            print('%s' % i, end='\t')
        for j in files:
            print('%s' % j, end='\t')
        print()


if __name__ == '__main__':
    lsdir(sys.argv[1])


















