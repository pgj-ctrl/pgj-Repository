f1 = open('/tmp/passwd','rb')
f2 = open('/tmp/cpp','wb')

data = f1.read(10)
# f2.write(data)
#
# f1.close()
# f2.close()

while len(f1.read(10)):
    f2.write(data)
else:
    f1.close()
    f2.close()