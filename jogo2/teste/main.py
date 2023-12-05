from jogo import Jogo
from menu import MenuPrincipal, MenuSkins

if __name__ == "__main__":
    jogo = Jogo()
    jogo.mudar_estado(MenuPrincipal())
    jogo.executar()
