import pygame
import sys
from constantes import *
from menu import mostrar_menu

def main():
    pygame.init()
    pantalla = pygame.display.set_mode(PANTALLA)
    pygame.display.set_caption("Preguntades")

    mostrar_menu(pantalla)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()