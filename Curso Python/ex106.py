print('\033[1;103m--------------------------')
print('  SISTEMA DE AJUDA PyHELP ')
print('--------------------------')


f = input(('\033[0;0mFunção ou Biblioteca >'))
print('\033[1;44m-----------------------------------')
print(f'Acessando o manual do comando {f}')
print('-----------------------------------')
print('\033[;7m')
print(f'{help(f)}')