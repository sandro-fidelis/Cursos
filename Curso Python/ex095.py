jogador = {}
atletas = []
gols = []
total = []
while True:
  jogador['nome'] = str(input('Nome: '))
  partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
  for c in range(0,partidas):
      gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
  jogador['gols'] = gols[:]
  jogador['total'] = sum(gols)
  atletas.append(jogador.copy())
  gols.clear()
  jogador.clear()
  print('=' * 40)
  while True:
    cont = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if cont in 'SN':
      break
    print('ERRO! Digite apenas  S ou N: ')
  if cont == 'N':
    break
print('=' * 40)
print('COD   Nome       Gols       Total')
print('-' * 40)
for i, j in enumerate(atletas):
  print(f'{i:>3}', end =" ")
  for k, v in j.items():
   print(f'{str(v):<10}', end = '   ')
  print()
print('=' * 40)
while True:
  dados = int(input('Mostrar dados de qual jogador? [999 Encerra] '))
  print('-'* 40)
  if dados == 999:
      break
  for i, j in enumerate(atletas):
    if dados == i:
        print(f'== MOSTRANDO DADOS DO JOGADOR {j["nome"]}:')
        for i, d in enumerate(j["gols"]):
            print(f'   No jogo {i+1} fez {j["gols"][i]} gols.')
    if dados > i:
        print('ERRO! Digite um valor válido')
print('<<<< ENCERRANDO >>>>')
