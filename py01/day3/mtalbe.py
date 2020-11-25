n=int(input('you want to number: '))
k = n+1
p = k-1
for i in range(1,10):
    for j in range(p,k):
        print('%s*%s=%s' % (i,j,i*j),end='\t')
    print(end=' ')
print()
