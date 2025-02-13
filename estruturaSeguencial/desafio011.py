'''desafio 011

faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua area e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta,pinta uma área de 2m².'''

alt1 = int(input('informe a altura da parede: '))
larg1 = int(input('informe a largura da parede: '))

n = alt1 * larg1

pintar = n * 2

print(f'a quantidade de tinta necessaria para pintar a parede é:{pintar}litros por metro quadrado')