i = m20 = h = mi = 0
while True:
  print('='*19)
  print('CADASTRO DE PESSOAS')
  print('='*19)
  i = int(input('Idade: '))
  s = str(' ')
  while s not in 'MF':
    s = str(input('Sexo: [M/F] ')).strip().upper()[0]
  if i >= 18:
    mi = mi + 1
  if i < 20 and s == 'F':
    m20 = m20 + 1
  if s == 'M':
    h = h + 1
  cont = str(' ')
  while cont not in 'SN':
    cont = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
  if cont == 'N':
    break
print('='*19)
print(f'Mulheres com menos de 20 anos. Total {m20}')
print(f'Homens. Total {h}')
print(f'Mais de 18 anos. Total {mi}')
print('Fim')
