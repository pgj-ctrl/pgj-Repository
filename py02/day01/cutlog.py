# from datetime import datetime
import datetime
k = '%Y-%m-%d %H:%M:%S'
t9 = datetime.datetime.strptime('2019-05-15 09:00:00',k)
t12 = datetime.datetime.strptime('2019-05-15 12:00:00',k)

with open ('aaa.txt') as fobj:
    for line in fobj:
        t = datetime.datetime.strptime(line[:19],k)
        # if t9 <= t <= t12:
        #     print(line,end='')
        if t > t12:
            break
        if t >= t9:
            print(line,end='')
