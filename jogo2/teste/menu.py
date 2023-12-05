import pygame
import sys
from jogo import Jogo

class EstadoMenu:
    def exibir_menu(self, tela):
        pass

    def processar_eventos(self, eventos):
        pass

    def realizar_acao(self, opcao):
        pass

class MenuPrincipal(EstadoMenu):
    def exibir_menu(self, tela):
        fonte_menu = pygame.font.Font(None, 36)
        opcoes = ["Jogar", "Skins", "Sair"]
        altura_opcao = 50
        posicao_y = 200

        for opcao_texto in opcoes:
            texto = fonte_menu.render(opcao_texto, True, (255, 255, 255))
            posicao = (200, posicao_y)
            tela.blit(texto, posicao)
            posicao_y += altura_opcao

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 200 <= mouse_x <= 400 and 200 <= mouse_y <= 250:
                    self.realizar_acao("Iniciar Jogo")
                elif 200 <= mouse_x <= 400 and 250 <= mouse_y <= 300:
                    self.realizar_acao("Abrir Skins")
                elif 200 <= mouse_x <= 400 and 300 <= mouse_y <= 350:
                    self.realizar_acao("Sair do Jogo")

    def realizar_acao(self, opcao):
        print(f"Ação: {opcao}")
        if opcao == "Iniciar Jogo":
            jogo.mudar_estado(MenuSkins())
        elif opcao == "Abrir Skins":
            jogo.mudar_estado(MenuSkins())
        elif opcao == "Sair do Jogo":
            sys.exit()

class MenuSkins(EstadoMenu):
    def exibir_menu(self, tela):
        fonte_menu = pygame.font.Font(None, 36)
        opcoes = ["Skin 1", "Skin 2", "Voltar"]
        altura_opcao = 50
        posicao_y = 200

        for opcao_texto in opcoes:
            texto = fonte_menu.render(opcao_texto, True, (255, 255, 255))
            posicao = (200, posicao_y)
            tela.blit(texto, posicao)
            posicao_y += altura_opcao

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 200 <= mouse_x <= 400 and 200 <= mouse_y <= 250:
                    self.realizar_acao("Selecionar Skin 1")
                elif 200 <= mouse_x <= 400 and 250 <= mouse_y <= 300:
                    self.realizar_acao("Selecionar Skin 2")
                elif 200 <= mouse_x <= 400 and 300 <= mouse_y <= 350:
                    self.realizar_acao("Voltar ao Menu Principal")

    def realizar_acao(self, opcao):
        print(f"Ação: {opcao}")
        if opcao == "Selecionar Skin 1":
            jogo.mudar_estado(MenuPrincipal())
        elif opcao == "Selecionar Skin 2":
            jogo.mudar_estado(MenuPrincipal())
        elif opcao == "Voltar ao Menu Principal":
            jogo.mudar_estado(MenuPrincipal())
