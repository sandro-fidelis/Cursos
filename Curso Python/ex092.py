from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
data = date.today()
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['idade'] = data.year - dados['nascimento']
dados['ctps'] = int(input('Carteira de Trabalho: (0 Não tem) '))
if dados['ctps'] != 0:
  dados['contratação'] = int(input('Ano de contratação: '))
  dados['salário'] = float(input('Salário: '))
  dados['aposentadoria'] = (dados['contratação'] - dados['nascimento']) + 35
  print('='*30)
else:
  print('=' * 30)
for k, v in dados.items():
  print(f'{k} tem valor {v}')