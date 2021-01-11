#Exercício feito com WHILE
'''n = int(input('Digite o número: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:
  print('{} '.format(c),end = '')
  print('x ' if c != 1 else '= ', end = '')
  f = f * c
  c = c-1
print(f)'''

#Exercícip feito com FOR
n = int(input('Digite um número para ver seu fatorial : '))
c = n
f = 1
print('Claculando {}!= '.format(n),end = '')
for c in range (c,0, -1):
  print('{}'.format(c),end = '')
  print(' x ' if c > 1 else ' = ', end = '')
  f = f * c
print(f)

