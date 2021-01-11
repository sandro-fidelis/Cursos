from time import sleep
def maior(*num):
    cont = maior = 0
    print('=' * 30)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v}', end = ' ', flush=True)
        sleep(1)
        if cont == 0:
            maior = cont
        else:
            if cont > maior:
                maior = cont
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(1, 5, 7, 8, 20, 30)
maior(2, 10, 15)
maior(1, 2)
maior(0)
maior()