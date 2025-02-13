'''Desafio 013

faça um algoritmo que leia o salário de um funcionatio e mostre seu novo salário,com 15% de aumento.'''
s1 = float(input('informe o salario do funcionario: '))
s1Novo = s1 + (s1/100 * 15)
print(f"o novo salario do funcionario com 15 % de aumento é:{s1Novo}")
