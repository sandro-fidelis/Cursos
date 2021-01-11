'''def leiaDinheiro(msg):
    p = input(msg).replace(',','.').strip()
    while p.isalpha() or p == '':
        print(f'ERRO {p} não é um preço válido' )
        p = input(msg)
    else:
        return float(p)'''


#GUANABARA
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: {entrada} é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)