# n = 0
#
# # b = int(range(1,11))
# for i in range(11):
#     print(n)
#     n += i
# print(n)


fib = [0,1]
for i in range(8):
    fib.append(fib[-1] + fib[-2])

print(fib)
print('总共',len(fib))