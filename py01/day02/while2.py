result = 0
i = 1

while i < 100:
    i += 1
    if i % 2 == 1:
        continue
    else:
        result += i
print(result)


