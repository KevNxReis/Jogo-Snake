import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((600, 400))

skin1 = 1
skin2 = 2
skin3 = 3

def set_skin(skin_value):
    print(f"Skin selecionada: {skin_value}")

def rodar_jogo():
    print("Iniciar o jogo...")

def menu_skins():
    skin_menu._open()

def selecionar_skin(value, skin_menu):
    set_skin(value)
    skin_menu._close()

mainmenu = pygame_menu.Menu('Jogo da Pitom', 600, 400, theme=themes.THEME_ORANGE)
mainmenu.add.text_input('Nick_Name: ', default='username', maxchar=20)
mainmenu.add.button('Jogar', rodar_jogo)
mainmenu.add.button('Skin', menu_skins)
mainmenu.add.button('Sair', pygame_menu.events.EXIT)

skin_menu = pygame_menu.Menu('Selecione a Skin', 600, 400, theme=themes.THEME_ORANGE)
skin_menu.add.button('Skin 1', action=pygame_menu.events.PYGAME_MENU_BACK, args=('skin1',))
skin_menu.add.button('Skin 2', action=pygame_menu.events.PYGAME_MENU_BACK, args=('skin2',))
skin_menu.add.button('Skin 3', action=pygame_menu.events.PYGAME_MENU_BACK, args=('skin3',))

mainmenu.mainloop(surface)
