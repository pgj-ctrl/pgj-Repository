s1 = 'abcd'
names = ['tom','jerry','jack','rose']
nums = (10, 8,20)
d1 = {'name': 'nb', 'age': 19}

for hh in s1:
    print(hh)
print('*' * 30)

for ww in names:
    print(ww)
print('#' * 30)

for tt in nums:
    print(tt)
print('(' * 30)

for i in d1:
    print(i ,d1[i])
print('nb' * 30)


n = 0
for i in range(1, 10000001):
    n += i
print(n)