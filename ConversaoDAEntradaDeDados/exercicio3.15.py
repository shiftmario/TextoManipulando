'''escreva um programa para calcular a 
redução do tempo de vida
de um fumante.
pergunte a quantidade de cigarros fumados
por dia e quantos anos ele já fumou.
considere que um fumante perde 10 minutos 
de vida a cada cigarro,e calcule quantos
 dias de vida um fumante perderá.
 Exiba o total em dias.
'''

fumados = int(input('digite quantos cigarros vc fuma por dia: '))
ano1 = int(input('informe quantos anos vc fuma: '))

diasVida = (fumados - ano1) * 10

print(f'você como fumante perderá de vida:{diasVida} dias')