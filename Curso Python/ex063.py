print('='*22)
print('SEQUÊNCIA DE FIBONACCI')
print('='*22)
n = int(input('Quantos termos voçê quer mostar: '))
n1 = 0
n2 = 1
n3 = 0
c = 0
print('{} '.format(n3), end = '')
while c < n-1:
  n3 = n1 + n2
  print('-> {} '.format(n3),end = '')
  n2 = n1
  n1 = n3
  c = c + 1
print('FIM')