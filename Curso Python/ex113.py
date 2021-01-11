'''def leiaInt(msg):
    while True:
        try:
            i = (input(msg))
            return int(i)

        except ValueError:
            print('Erro! Digite um número inteiro válido!')
        if i.isnumeric():
            break


def leiaFloat(msg):
    while True:
        try:
            r = input(msg)
            return float(r)

        except ValueError:
            print('ERRO! Digite um número real válido!')

        if r.isnumeric():
            break'''

#GUANABARA

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor digite um número inteiro válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[031mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('\033[031mERRO: por favor digite um número real válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[031mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
