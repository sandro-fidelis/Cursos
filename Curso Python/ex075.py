t = (int(input('Digite o 1° valor: ')),
int(input('Digite o 2° valor: ')),
int(input('Digite o 3° valor: ')),
int(input('Digite o 4° valor: ')))
print(f'Você digitou os valores {t}')
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t:
  print(f'O número 3 foi digitado na {t.index(3)+1}ª posição')
else:
  print(f'O número 3 não foi digitado em nenhuma posição')
par = 0
for c in t :
  if c % 2 == 0:
    par = par + 1
print(f'Foram digitados {par} números pares ')
print(f'Os valores pares digitados foram ',end='')
for c in t:
  if c % 2 == 0:
    print(c, end = ',')
