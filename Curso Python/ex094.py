dados = []
pessoa = {}
sidade = media = 0
while True:
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    print('ERRO! Por favor digite M ou F.' )
  pessoa['idade'] = int(input('Idade: '))
  sidade += pessoa['idade']
  dados.append(pessoa.copy())
  while True:
    cont = str(input('Quer continuar? [S/N] ')).upper()[0]
    if cont in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')
  if cont == 'N':
    break
print(dados)
print('=' * 40)
print(f'O grupo tem {len(dados)} pessoas')
media = sidade / len(dados)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram: ',end = '')
for p in dados:
  if p['sexo']== 'F':
    print(p['nome'])
print(f'Lista de pessoas que estão acima da média: ',end ="")
print()
for p in dados:
  print('    ')
  for k, v in p.items():
    print(f'{k} = {v}',end = ' : ')
  print()
print()
print('<<< ENCERRANDO >>>')