jogador = {}
gols = []
total = []
tot = 0
jogador['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
print('=' * 40)
jogador['gols'] = gols
for t in gols:
  tot += t
total.append(tot)
jogador['total'] = tot
print(jogador)
print('=' * 40)
for k, v in jogador.items():
  print(f'O campo {k} tem valor {v}')
print('=' * 40)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(gols):
  print(f'Na partida {k+1}, fez {v} gols ')
print(f'Foi um total de {total[0]} gols')
