def area(l, c):
  a = (l * c)
  print(f'A área de um terreno {l} X {c} é : {a} m².')


#PROGRAMA PRINCIPAL
print('  CONTROLE DE TERRENOS')
print('-'*24)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)

