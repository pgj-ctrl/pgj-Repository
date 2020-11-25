s1 = 'abcd'
names = ['tom','jerry','jack','rose']
nums = (10,8,20)
d1 = {'name': 'nb','age': 10}

for i in s1:
    print(i)
    print('3' * 30)
for t in names:
    print(t)
    print('4' * 30)
for y in nums:
    print(y)
    print(')' * 30)
for u in d1:
    print(u)
    print('+' * 30)

fib = [0,1]
n = int(input('you wnat have: '))
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)
print('总共:',len(fib))