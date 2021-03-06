from time import strftime
import  os
import tarfile
import hashlib
import pickle
import sys
import work
t = strftime("%Y%m%d")
def full_backup(src,dst,md5file):
    "完全备份"
    #拼接出文件备份名
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src),t)
    fname = os.path.join(dst,fname)

    #打tar包
    tar = tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()
    #计算文件的MD5值
    md5dict = {}
    for path,folders,files in os.walk(src):
        for file in files:
            key = os.path.join(path,file)
            md5dict[key] = check_md5(key)

    #将MD5字典保存到文件中
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)
def incr_backup(src,dst,md5file):
    "增量备份"









def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb')as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon' or not os.path.exists(md5file):
        full_backup(src,dst,md5file)
    else:
        incr_backup(src,dst,md5file)



# mkdir -p /tmp/demo/backup
# cp -r /etc/security/ /tmp/demo/

