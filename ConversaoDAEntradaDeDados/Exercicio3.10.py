'''faça um programa que calcule
o aumento de um salário.
Ele deve solicitar o valor 
do salário e a procentagem do aumento
.Exiba o valor do aumento 
e do novo salário.'''

salario = float(input('informe o valor do salario: '))
novoSalario = float(input('informe o percentual do salario: '))

novoSalario = (salario + ((salario*salario)/100))
aumento =  novoSalario - salario

print(f'o novo salario foi: { novoSalario}, o aumento do salario foi:{aumento}')