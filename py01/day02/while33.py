result = 0
i = 1

while i < 100:
    i += 1
    if i % 2 : #整数除以2只会0或1，也就是真或者假
        continue
    else:
        result += i
print(result)