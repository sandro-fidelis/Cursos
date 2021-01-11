print('='*40)
frase = 'JOGA NA MEGA SENA'
print(f'{frase:^40}')
print('='*40)
import random
import time
jogo = [ ]
quant = int(input('Quantos jogos você quer que eu sorteie ? '))
print(f'============ SORTEANDO {quant} JOGOS ============')
c = 0
while c < quant:
    n = random.sample(range(1, 60), 6)
    jogo.append(n)
    time.sleep(1.5)
    print(f'{c+1}° Jogo: {sorted(jogo[c])}')
    c += 1

