vel = float(input('Qual a velocidade do veículo? '))
if vel > 80:
    print('MULTADO! ultrapassou o limíte de velocidade que é 80 Kmh')
    cal = float(vel - 80)
    val = float(7.00)
    mul = cal * val
    print('O valor da multa é R${:.2f}'.format(mul))
else:
    print('Tenha um bom dia e dirija sempre com segurança!')