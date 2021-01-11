v = float(input('Qual o valor do imóvel?: R$ '))
s = float(input('Qual o valor do salário dos compradores?: R$ '))
t = float(input('Em quantos anos serão dividos as parcelas? '))
m = t * 12
vm = v / m
ps = s/100*30
print('Quantidade de meses é {:.0f}'.format(m))
print('Valor limite de parcela é {:.2f}'.format(vm))
print('Valor aprovado da parcela do comprador é: {:.2f}'.format(ps))
if vm > ps:
    print('Financiamento NEGADO !, A parcela não pode passar de 30% do valor do salário')
else:
    print('Financiamento APROVADO')
