'''faça um programa que solicite o preço de uma
mercadoria e o percentual de desconto.
Exiba o valor do desconto a pagar.'''

mercadoria = float(input('informe o preço da mercadoria: '))
percentual = float(input('informe o percentual de desconto: '))

preco = (mercadoria + (mercadoria * percentual)/100)

descontoApagar =  preco - mercadoria

print(f'voce tera que pagar de desconto:{descontoApagar}')