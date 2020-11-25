# import hashlib
# import sys
#
# def check_md5(fname):
#     m = hashlib.md5()
#     with open(fname,'rb')as fobj:
#         while 1 :
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     print(check_md5(sys.argv[1]))

# import os
# from time import strftime
# import hashlib
# import pickle
# import tarfile
# def check_md5(fname):
#     m = hashlib.md5()
#     with open(fname, 'rb') as fobj:
#         while 1:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#
#     return m.hexdigest()
#
# def full_backup(src,dst,md5file):
#      fname = '%s_full_%s.tar.gz' % (os.path.basename(src),strftime("%Y%m%d"))
#      fname = os.path.join(dst,fname)
#
#      tar = tarfile.open(fname,'w:gz')
#      tar.add(src)
#      tar.close()
#
#      md5dict = {}
#      for path,folders,files in os.walk(src):
#          for file in files:
#              key = os.path.join(path,file)
#              md5dict[key] = check_md5(key)
#
#      with open(md5file,'wb')as fobj:
#          pickle.dump(md5dict,fobj)
#
# def incr_back(src,dst,md5file):
#     fname = '%s_incr_%s.tar.gz' % (os.path.basename(src),strftime('%Y%m%d'))
#     fanme = os.path.join(dst,fname)
#
#     md5dict = {}
#     for path,folders,files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5dict[key] = check_md5(key)
#
#     with open(md5file,'rb')as fobj:
#         old_md5 = pickle.load(fobj)
#
#     tar  = tarfile.open(fname,'w:gz')
#     for key in md5dict:
#         if old_md5.get(key) != md5dict[key]:
#             tar.add(key)
#     tar.close()
#
# if __name__ == '__main__':
#     src = '/tmp/demo/security'
#     dst = '/tmp/demo/backup'
#     md5file = '/tmp/demo/backup/md5.data'
#     if strftime('%a') == 'Mon' or not os.path.exists(md5file):
#         full_backup(src,dst,md5file)
#     else:
#         incr_back(src,dst,md5file)

# mkdir -p /tmp/demo/backup
# cp -r /etc/security/ /tmp/demo/

class Role:
    def __init__(self,name,weapon):
        self.name = name
        self.weapon= weapon
    def __str__(self):
        return '%s %s is me' % (self.name,self.weapon)
    def __call__(self):
        print('%s %s is me' % (self.name,self.weapon))

if __name__ == '__main__':
    t1 = Role('the','king')
    print(t1)
    t1()