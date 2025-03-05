'''escreva um prograa que leia 
a quantidade de dias,horas,minutos 
e segundos do usuário.
Calcule o total em segundos'''

d = int(input('dias'))
h = int(input('horas'))
m = int(input('minutos'))
s = int(input('segundos'))


total_segundos = (d * 24 * 3600 + h * 3600 + m * 60 + s)

print(f'o total de segundos do usuario é:{total_segundos}')