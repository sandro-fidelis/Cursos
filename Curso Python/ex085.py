lista = []
par = []
impar = []
for c in range(1,8):
  n = int(input(f'Digite o {c}° número: '))
  if n % 2 == 0:
    par.append(n)
  else:
    impar.append(n)
lista.append(par)
lista.append(impar)
print('='*40)
print(f'A lista completa é: {lista}')
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores ímpares digitados foram: {sorted(impar)}')

'''
#GUANABARA
num = [[],[]]
valor = 0
for c in range(1,8):
  valor = int(input(f'Digite o {c}° valor: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
    num[1].append(valor)
print('='*40)
print(f'Todos os valores digitados foram: {num}')
print(f'Os valore pares digitados foram: {sorted(num[0])}')
print(f'Os valore ímpares digitados foram: {sorted(num[1])}')'''
