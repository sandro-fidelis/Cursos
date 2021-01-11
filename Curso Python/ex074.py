from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os valores sorteados foram: ',end = '')
maior = menor = n[0]
for c in n:
  print(f'{c} ',end = '')
  if c > maior:
    maior  = c
  if c < menor:
    menor = c
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
print({max(n)})# formatação em python sem necessidade de if para verificar maior e menor
print({min(n)})

