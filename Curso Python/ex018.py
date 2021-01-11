from math import radians,sin, cos, tan
an = float(input('Digite o ângulo que voçê deseja: '))
se = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
co = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an,co))
tan = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,tan))


