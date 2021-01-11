lista0 = []
lista1 = []
lista2 = []
for c in range(0,3):
  lista0.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0,3):
  lista1.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0,3):
  lista2.append(int(input(f'Digite um valor para [2, {c}]: ')))
print('='*30)
print(lista0)
print(lista1)
print(lista2)
print('='*30)
for p in lista0:
  print(f'[ {p} ]',end = '')
print('\n',end = '')
for p in lista1:
  print(f'[ {p} ]',end = '')
print('\n', end = '')
for p in lista2:
  print(f'[ {p} ]',end = '')

'''
# GUANABARA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()
'''