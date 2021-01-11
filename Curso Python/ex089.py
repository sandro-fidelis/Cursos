alunos = []
dados = []
while True:
  dados.append(str(input('Nome: ')))
  dados.append(float(input('Nota 1: ')))
  dados.append(float(input('Nota 2: ')))
  alunos.append(dados[:])
  dados.clear()
  cont = str(input('Quer continuar? [S/N] '))
  if cont in 'Nn':
    break
print('=' * 40)
print('N°.    NOME      MEDIA')
print('----------------------')
for i, d in enumerate(alunos):
  print(f'{i:<4}{d[0]:^10}{(d[1]+d[2])/2:>6}')
print('='*40)
vernota = -1
while vernota != 999:
  vernota = int(input('Mostrar as notas de qual aluno? - (999 interompe)'))
  if vernota == 999:
    break
  for i,d in enumerate(alunos):
    if i == vernota:
      print(f'As notas de {d[0]} são: {d[1]} e {d[2]}')
print('FIM DO PROGRAMA')
