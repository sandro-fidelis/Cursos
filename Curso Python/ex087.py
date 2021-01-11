lista0 = []
lista1 = []
lista2 = []
par = 0
for c in range(0,3):
  lista0.append(int(input(f'Digite um valor para [0, {c}]: ')))
  if lista0[c] % 2 == 0:
    par += lista0[c]
for c in range(0,3):
  lista1.append(int(input(f'Digite um valor para [1, {c}]: ')))
  if lista1[c] % 2 == 0:
    par += lista1[c]
for c in range(0,3):
  lista2.append(int(input(f'Digite um valor para [2, {c}]: ')))
  if lista2[c] % 2 == 0:
    par += lista2[c]
print('='*30)
for p in lista0:
  print(f'[ {p:^5} ]',end = '')
print('\n',end = '')
for p in lista1:
  print(f'[ {p:^5} ]',end = '')
print('\n', end = '')
for p in lista2:
  print(f'[ {p:^5} ]',end = '')
print()
print('='*30)
print(f'A soma de todos os valores pares é {par}.')
soma = lista0[2] + lista1[2] + lista2[2]
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {max(lista1)}.')