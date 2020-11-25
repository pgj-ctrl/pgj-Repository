import time
u = 0
o = time.time()
for i in range(1,20000001):
    u += i
print(u)
k = time.time()
j = k - o
print('%1f' % j)
