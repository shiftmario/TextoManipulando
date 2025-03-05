'''escreva um programa que calcule
o tempo de uma viagem de carro.
Pergunte a distância a pecorrer e a 
velocidade média esperada para a viagem.
'''

'''distancia = float(input('digite a distancia pecorrida em km/h'))
vm = float(input('digite a velocidade media do carro'))
tempo = distancia / vm

tempo_s = int(tempo * 3600)
horas = int(tempo_s/ 3600)
tempo_s int(tempo_s_% 3600)
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

print(f'tempo estimado em horas:{tempo, tempo_s,horas,minutos,segundos}')'''

distancia = float(input('digite a distancia percorrida pelo carro: '))
vm = float(input('digite a velocidade do carro: '))
tempo = float(input('digite o tempo que se passou no percurso: '))
horas = float(input('digite as horas que foram pecorridas durante o percurso: '))
minutos = float(input('digite os minutos'))
segundos = float(input('digite os segundo que se passaram durante o percurso'))
print(f'tempo{tempo * 3600 + horas % 3600 + minutos / 60 + segundos / vm }')