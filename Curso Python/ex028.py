from random import randint
from time import sleep
print('Vou pensar em um número de 0 a 5')
n = randint(0,5)
ne = int(input('Qual número eu pensei? '))
print('PRCESSANDO...')
sleep(3)
if n==ne:
    print('Acertou eu pensei no número {} '.format(n))
else:
    print('ERRRROOOUUU!! Eu pensei no número {}'.format(n))

