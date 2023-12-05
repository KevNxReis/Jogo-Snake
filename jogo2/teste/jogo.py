import pygame
import sys

class Jogo:
    def __init__(self):
        self.estado_atual = None

    def mudar_estado(self, novo_estado):
        self.estado_atual = novo_estado

    def executar(self):
        pygame.init()
        largura, altura = 800, 600
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Meu Jogo")

        clock = pygame.time.Clock()

        while True:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    sys.exit()

            self.estado_atual.processar_eventos(eventos)
            self.estado_atual.exibir_menu(tela)

            pygame.display.flip()
            clock.tick(30)
