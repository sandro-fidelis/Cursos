k = float(input('Quantos Km foram percorridos? '))
d = int(input('Quantos dias o carro foi utilizado? '))
km = k * 0.15
di = d * 60
t = km + di
print('O valor total a ser pago pelo aluguel é:R$ {:.2f}'.format(t))
