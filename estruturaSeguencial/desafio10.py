'''crie um programa que leia quanto dinheiro uma pessoa 
tem na carteira e mostre quantos dólares ele pode comprar.'''

carteira = int(input('informe quanto você tem na carteira:  '))

dolar = 3.47

conversao = (carteira / dolar)
print(f'o valor de sua carteira para comprar dolares é:{conversao :.2f}')
