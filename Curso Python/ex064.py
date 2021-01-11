s = nd = n = 0
n = int(input('Digite um números ou [999] para encerrar: '))
while n != 999:
    s = s + n
    nd = nd + 1
    n = int(input('Digite um números ou [999] para encerrar: '))
print('Foram digitados {} números:'.format(nd))
print('A soma de todos os números digitados é {}'.format(s))
