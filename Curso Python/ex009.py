n = int(input('Qual tabuada deseja ver: '))
c=1
print(11*'=')
while c <= 10:
    print('{} x {:2} = {}'.format(n,c,c*n))
    c += 1
print(11*'=')
