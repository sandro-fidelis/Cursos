n = str(input('Digite seu nome completo: ')).strip()
separado = n.split()
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu último nome é {}'.format(separado[len(separado)-1]))
