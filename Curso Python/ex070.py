print('===============')
print('LOJA TATI & CIA')
print('===============')
vt = mil = barato = 0
nomebarato = str(' ')
pd = 0 #preço digitados
while True:
  nome = str(input('Produto: '))
  preco = float(input('Preço: R$ '))
  vt = vt + preco
  pd = pd + 1
  if preco >= 1000:
    mil = mil + 1
  if pd == 1:
    barato = preco
    nomebarato = nome
  else:
    if preco < barato:
      barato = preco
      nomebarato = nome
  cont = str(' ')
  while cont not in 'SN':
    cont = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
  if cont == 'N':
    break
print(f'O valor total da compra é : R$ {vt:.2f} Reais')
print(f'{mil} produtos custam mais de R$ 1.000,00 Reais')
print(f'O produto mais barato foi {nomebarato} que custa R$ {barato:.2f} Reais')
