maior = float()
menor = float()
for c in range(1,4):
  peso = float(input('Digite o peso da {} pessoa: '.format(c)))
  if c == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print('O maior peso lido é {}Kgs'.format(maior))
print('O menor peso lido é {}Kgs'.format(menor))