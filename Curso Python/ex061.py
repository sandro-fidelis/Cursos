p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
#decimo = p + (10 - 1).r
c = 1
print('Os 10 primeiros termos desta PA é:')
while c < 11:
  print('{} -> '.format(p),end='')
  p = p + r
  c = c + 1
print('FIM')