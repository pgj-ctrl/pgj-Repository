import re

def tongjiip():
    u = {}
    with open('access_log')as fobj:
        l1 = set(fobj.readlines())
    for i in list(l1):
        m = re.search('^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+|^:..',i)
        u[m.group()] = 0
    with open('access_log')as fobj:
        while 1:
            data = fobj.readline()
            if not data:
                break
            f = re.search('^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+|^:..',data)
            if f.group() in u.keys():
                  u[f.group()] = u[f.group()] + 1
    print(u)


if __name__ == '__main__':
    tongjiip()