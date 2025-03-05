import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Raquetes
raquete_largura = 10
raquete_altura = 100
raquete_velocidade = 5

raquete_jogador = pygame.Rect(50, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)
raquete_computador = pygame.Rect(largura - 50 - raquete_largura, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)

# Bola
bola_largura = 10
bola_velocidade_x = 5
bola_velocidade_y = 5

bola = pygame.Rect(largura // 2 - bola_largura // 2, altura // 2 - bola_largura // 2, bola_largura, bola_largura)

# Pontuação
pontuacao_jogador = 0
pontuacao_computador = 0
fonte = pygame.font.Font(None, 36)

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Movimento da raquete do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete_jogador.y > 0:
        raquete_jogador.y -= raquete_velocidade
    if teclas[pygame.K_s] and raquete_jogador.y < altura - raquete_altura:
        raquete_jogador.y += raquete_velocidade

    # Movimento da raquete do computador
    if bola.y < raquete_computador.y + raquete_altura // 2:
        raquete_computador.y -= raquete_velocidade
    if bola.y > raquete_computador.y + raquete_altura // 2:
        raquete_computador.y += raquete_velocidade

    # Movimento da bola
    bola.x += bola_velocidade_x
    bola.y += bola_velocidade_y

    # Colisão com as paredes
    if bola.y <= 0 or bola.y >= altura - bola_largura:
        bola_velocidade_y *= -1

    # Colisão com as raquetes
    if bola.colliderect(raquete_jogador) or bola.colliderect(raquete_computador):
        bola_velocidade_x *= -1

    # Pontuação
    if bola.x < 0:
        pontuacao_computador += 1
        bola.x = largura // 2 - bola_largura // 2
        bola.y = altura // 2 - bola_largura // 2
        bola_velocidade_x *= -1
    elif bola.x > largura - bola_largura:
        pontuacao_jogador += 1
        bola.x = largura // 2 - bola_largura // 2
        bola.y = altura // 2 - bola_largura // 2
        bola_velocidade_x *= -1

    # Desenho na tela
    tela.fill(preto)
    pygame.draw.rect(tela, branco, raquete_jogador)
    pygame.draw.rect(tela, branco, raquete_computador)
    pygame.draw.ellipse(tela, branco, bola)

    # Desenho da pontuação
    texto_jogador = fonte.render(str(pontuacao_jogador), True, branco)
    texto_computador = fonte.render(str(pontuacao_computador), True, branco)
    tela.blit(texto_jogador, (largura // 4, 20))
    tela.blit(texto_computador, (largura * 3 // 4, 20))

    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()