nome = 'Eugênio Coelho'
altura = 1.76
peso = 84
imc = peso / altura ** 2 # IMC = peso / (altura x altura)

print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu IMC é ')
print(imc)

# f-strings
linha_1 = f'{nome} tem {altura:.2f}m de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


# Eugênio Coelho tem 1.76 de altura,
# pesa 84 quilos e seu IMC é
# 27.117768595041323