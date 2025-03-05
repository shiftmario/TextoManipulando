import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bola Quicando")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Bola
raio_bola = 25
posicao_bola_x = largura // 2
posicao_bola_y = altura // 2
velocidade_bola_x = 5
velocidade_bola_y = 5

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Movimento da bola
    posicao_bola_x += velocidade_bola_x
    posicao_bola_y += velocidade_bola_y

    # Colisão com as paredes
    if posicao_bola_x <= raio_bola or posicao_bola_x >= largura - raio_bola:
        velocidade_bola_x *= -1
    if posicao_bola_y <= raio_bola or posicao_bola_y >= altura - raio_bola:
        velocidade_bola_y *= -1

    # Desenho na tela
    tela.fill(preto)
    pygame.draw.circle(tela, branco, (posicao_bola_x, posicao_bola_y), raio_bola)

    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()