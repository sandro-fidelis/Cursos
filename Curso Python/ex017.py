'''import math
n1 = float(input('Digite o valor do cateto oposto:'))
n2 = float(input('Digite o valor do cateto adjacente:'))
r = n1**2 + n2**2
h = math.sqrt(r)
print('A hipotenusa é igual a {:.2f}'.format(h))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cate adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
