import sys
# print(sys.argv)
# src_fname = sys.argv[1]
# det_fname = sys.argv[2]

def cp(src_fname,det_fname):
    src_fobj = open(src_fname,'rb')
    dst_fobj = open(det_fname, 'wb')
    # with open(src_fname,'rb') as src_fobj:
    # with open(det_fname,'wb') as dst_fobj:
    while 1:
        data = src_fobj.read(4096)
        if not data:
            break
        dst_fobj.write(data)

    # src_fobj.close()
    # dst_fobj.close()
    return det_fname
cp(sys.argv[1],sys.argv[2])