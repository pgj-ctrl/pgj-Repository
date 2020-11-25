import re

class CountPatt:

    def count_patt(self,fname,patt):
        result = {}
        cpatt = re.compile(patt)
        with open(fname)as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    result[key] = result.get(key, 0) + 1
        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Chrome|MSIE|Firefox'
    cp1 = CountPatt()
    result1 = cp1.count_patt(fname, ip)
    result2 = cp1.count_patt(fname, br)
    print(result1)
    print(result2)