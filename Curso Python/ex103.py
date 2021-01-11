def ficha(n ='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('-'*30)
n = str(input('Digite o nome do jogador: '))
g = str(input(f'Número de Gols: ' ))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(g = g)
else:
    ficha(n,g)