soma = 0
media = 0
velho = 0
nomevelho = ''
totmenos20 = 0
s = str()
for c in range(1,5):
    print('=========== {} PESSOA ==========='.format(c))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F]?: '))
    soma += i
    if c == 1 and s in 'Mm':
        velho = i
        nomevelho = n
    if s in 'Mm' and i > velho:
        velho = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        totmenos20 += 1
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e o seu nome é {}'.format(velho,nomevelho))
print('O total de mulheres com menos de 20 anos é: {}'.format(totmenos20))