matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
par = soma = maior = 0

for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=' * 40)
for l in range(0,3):
  for c in range(0,3):
    print(f'[ {matriz[l][c]:^5} ]',end = '')
    if matriz[l][c] % 2 == 0:
      par += matriz[l][c]
  print()
print('=' * 40)
print(f'A soma de todos os valores pares é {par}.')
#soma = matriz[0][2] + matriz[1][2] + matriz[2][2] 'MINHA SOLUÇÃO'
for l in range(0,3):
  soma += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma}.')
# print(f'O maior valor da segunda linha é {max(matriz[1])}.')'MINHA SOLUÇÃO'
for c in range(0,3):
  if c == 0:
    maior = matriz[1][c]
  elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')