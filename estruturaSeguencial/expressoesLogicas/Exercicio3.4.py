'''escreva um expressão para determinar se uma pesoa deve ou não pagar imposto
.Cosidere que pagam imposto pessoas cujo salario é maior que r$1.200.00'''

n1  = int(input('digite seu salario: '))

if n1 > 1.200:
    print('usuario paga imposto:')
elif n1 < 1.200:
    print('usuario não paga imposto: ')
else:
    print('não paga imposto: ')