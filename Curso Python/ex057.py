s = str(input('Digite o sexo: [M/F]: ')).strip().upper()[0]
while s not in 'MF':
  s = str(input('ERRO!! Sexo inválido digite novamente: ')).strip().upper()[0]
print('Sexo {}. Dados inseridos com sucesso'.format(s))