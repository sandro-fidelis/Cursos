v = float(input('Digite o valor a ser pago: R$ '))
c = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if c == 1:
    vf = v - (v * 10 / 100)
elif c == 2:
    vf = v - (v * 5/ 100)
elif c == 3:
    vf = v
    p = vf / 2
    print('A sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(p))
elif c == 4:
    vf = v + (v * 20 / 100)
    p = int(input('Em quantas parcelas? '))
    pt = vf / p
    print('A sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(p,pt))
else:
    vf = 0
    print('OPÇÃO INVÁILIDA DE PAGAMENTO. tente novamente')
print('A sua compra de R${:.2F} vai custar R${:.2f} reais no final'.format(v,vf))
