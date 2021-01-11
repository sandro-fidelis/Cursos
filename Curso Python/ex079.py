v = []
while True:
  n = (int(input('Digite um valor: ')))
  if n not in v:
    v.append(n)
    print('Adicionado com sucesso')
  else:
    print('Valor já existe, Não pode ser adicionado')
  r = str(input('Quer continuar? [S/N] '))
  if r in 'Nn':
    break
print('='*40)
print(f'Os números digitados foram {sorted(v)}')