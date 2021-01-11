def leiaInt(n):
    while True:
        n = str(input(n))
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}')
            break
        else:
            print('ERRO! Digite um número: ')


n = leiaInt('Digite um número: ')

print('=' * 40)


# GUANABARA
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')

