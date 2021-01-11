dados = []
pessoas = []
mai = men = 0
while True:
  dados.append(str(input('Nome: ')))
  dados.append(float(input('Peso: ')))
  if len(pessoas) == 0:
    mai = men = dados[1]
  else:
    if dados[1] > mai:
      mai = dados[1]
    if dados[1] < men:
      men = dados[1]
  pessoas.append(dados[:])
  dados.clear()
  cont = str(input('Quer continuar? [S/N] '))
  if cont in 'Nn':
    break
print('='*40)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso é de {mai} Kgs de,',end = '')
for p in  pessoas:
  if p[1] == mai:
    print(f' [{p[0]}], ')
print(f'O menor peso é de {men} kgs de,', end = '')
for p in pessoas:
  if p[1] == men:
    print(f' [{p[0]}], ')