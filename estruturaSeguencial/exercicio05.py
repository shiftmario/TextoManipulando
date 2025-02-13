'''Desafio 005

faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.'''

num1 = int(input('digite um numero: '))

antecessor = num1 - 1
sucessor = num1 + 1

print(f'numero:{num1} antecessor:{antecessor},sucessor:{sucessor}')