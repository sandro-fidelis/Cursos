pt = int(input('Digite o Primeiro Termo: '))
ra = int(input('Digite a razão: '))
decimo = pt + (10-1) * ra
for c in range(pt,decimo+1,ra):
    print('{} '.format(c), end='-> ')
print('ACABOU')
