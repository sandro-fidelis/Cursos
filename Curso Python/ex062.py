p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
t = ()
termo = 0
while c < 10:
  print('{} -> '.format(p),end = '')
  p = p + r
  termo = c + 1
  c = c + 1
print('PAUSA', end='')
while t != 0:
  t = int(input('\nQuer ver mais termos?, Quantos?'
  '\nDigite "0" para TERMINAR ou "O VALOR" para CONTINUAR '))
  c2 = 0
  while c2 < t:
    print('{} -> '.format(p),end = '')
    p = p + r
    c2 = c2 + 1
    termo = termo + 1
  print('PAUSA', end='')
print('\nForam mostrados {} termos'.format(termo))