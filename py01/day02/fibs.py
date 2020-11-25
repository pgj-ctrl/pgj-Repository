fib = [0,1]
n = int(input('你想要的几项: '))
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)
print('总共:',len(fib))