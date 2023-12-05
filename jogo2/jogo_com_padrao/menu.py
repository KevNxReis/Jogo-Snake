from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes


pygame.init()
surface = pygame.display.set_mode((600,400))

skin1 = 1
skin2 = 2
skin3 = 3

def set_skin(skin_value):
    print(f'skin seleconada: {skin_value}')
    
def rodar_jogo():
    print('iniciar jogo...')

def menu_skins():
    mainmenu._open(skin)
    
def selecionar_skin(value, skin_menu):
    set_skin(value)
    skin_menu._close()


mainmenu = pygame_menu.Menu('Jogo da Pitom', 600, 400,
                            theme = themes.THEME_ORANGE)
mainmenu.add.text_input('Nick Name: ', default= 'username', maxchar=20)
mainmenu.add.button ('Jogar', rodar_jogo)
mainmenu.add.button ('Skin', menu_skins)
mainmenu.add.button ('Sair', pygame_menu.events.EXIT)

skin = pygame_menu.Menu ('Selecione a Skin', 600,400,
                        theme=themes.THEME_ORANGE)
skin.add.button('Skin 1')
skin.add.button('Skin 2')
skin.add.button('Skin 3')

mainmenu.mainloop (surface)



