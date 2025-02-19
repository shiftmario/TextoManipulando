'''exercicio3.6 escreva uma expressão que será utilizada para decidir
se um aluno foi ou não aprovado.Para ser aprovado,todas as
médias do aluno devem ser vaiores que 7.
Considere que o aluno cursa apenas três matérias,e que a nota de cada uma está armazenada nas seguintes
variaveis:matéria1,matéria2 e matéria3.'''


materia1 = int(input('digite a nota da primeira matéria:'))
materia2 = int(input('digite a nota da segunda matéria: '))
materia3 = int(input('digite a nota da terceira materia: '))

if materia1 < 7 and materia2 < 7 and materia3 < 7:
    print('reprovado')

elif materia1 >= 7 and materia2 >= 7 and materia3 >= 7:
    print('aprovado')
