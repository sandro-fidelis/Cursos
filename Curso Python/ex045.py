from random import randint
from time import sleep
palavras = ("PEDRA", "PAPEL", "TESOURA")
c = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPAEL
[ 2 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
if j > 2:
  print('ERRO!!! JOGADA INVÁLIDA TENTE NOVAMENTE')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('=' * 30)
    print('Você escolheu: {}'.format(palavras[j]))
    print('O computador escolheu: {}'.format(palavras[c]))
    print('=' * 30)
    if j == c:
         print('EMPATE')
    elif j == 2 and c == 0 or\
         j == 0 and c == 1 or \
         j == 1 and c == 2:
         print('O computador VENCEU' )
    else:
        print('VOÇÊ VENCEU')