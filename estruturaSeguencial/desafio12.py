'''Desafio 012
 faça um algoritmo que leia o preço de um produto 
 e mostre seu no preço,com 5% de desconto.'''

preco = float(input("infome o preço do produto: "))

precoNovo = preco - (preco / 100 * 5 )

print(f"o novo preço do produto ,com 5 porcento de desconto é {precoNovo}")