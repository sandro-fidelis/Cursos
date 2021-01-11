n = int(input('Digite um número: '))
cont = 0
for c in range(1,n+1):
    if n%c == 0:
        cont += 1
        print('\33[34m', end='')
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisível {} vezes'.format(n, cont))
if cont ==2:
    print('O número {} é PRIMO'.format(n))
else:
    print('O número {} NÃO é primo'.format(n))
