'''escreva um programa qie pergunte a quantidade 
de km percorridos por um carro alugado 
pelo usuário,assim como a guantidade de dias 
pelos quais o carro foi alugado.calcule o 
preço a pagar,sabendo que o carro custa 
r$ 60 por dia e r $0,15 por km rodado.'''


km1 = float(input('informe q quantidade de kilometros pecorrido pelo carro: '))
aluguel = float(input('informe a quantidades de dias do aluguel do carro: '))

km = 60 * km1 + (0.15 * aluguel)

print(f"o preço a pagar do aluguel é {km}")