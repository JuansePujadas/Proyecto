import pygame
import sys
from constantes import *

pygame.init()

pantalla = pygame.display.set_mode(PANTALLA)  # Crea la ventana

iniciar_img = pygame.image.load("Proyecto\imagenes\Iniciar.png").convert()
opciones_img = pygame.image.load("Proyecto\imagenes\Opciones.png").convert()
puntuaciones_img = pygame.image.load("Proyecto\imagenes\Puntuaciones.png").convert()  # Cargar y convertir las imágenes
salir_img = pygame.image.load("Proyecto\imagenes\Salir.png").convert()
config_img = pygame.image.load("Proyecto\imagenes\config.png").convert()

rect_iniciar = pygame.Rect(105, 44, 295, 120)
rect_opciones = pygame.Rect(110, 177, 280, 80)
rect_puntuaciones = pygame.Rect(80, 275, 340, 100)   # Definir rectángulos
rect_salir = pygame.Rect(150, 390, 210, 80)
rect_config = pygame.Rect(10, 10, 30, 30)

def clic_dentro_rect(rect, pos):    # Función para verificar si un punto está dentro de un rectángulo
    return rect.collidepoint(pos)

def abrir_nueva_ventana(color):   # Función para verificar si un punto está dentro de un rectángulo
    pantalla.fill(color)
    pygame.display.flip()
    pygame.time.wait(2000)  # Espera 2 segundos para simular el cambio de ventana

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # Nos permite cerrar el programa apretando en la "X"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if clic_dentro_rect(rect_iniciar, pos):
                abrir_nueva_ventana(COLOR_ROJO)
            elif clic_dentro_rect(rect_opciones, pos):
                abrir_nueva_ventana(COLOR_NEGRO)
            elif clic_dentro_rect(rect_puntuaciones, pos):
                abrir_nueva_ventana(COLOR_VERDE)
            elif clic_dentro_rect(rect_config, pos):
                abrir_nueva_ventana(COLOR_AZUL)
            elif clic_dentro_rect(rect_salir, pos):
                sys.exit()  # Salir del programa

    pantalla.fill(COLOR_NEGRO)

    # Dibujar rectángulos (Dejo esto comentado para ver donde se esta trabajando)
#    pygame.draw.rect(pantalla, COLOR_BLANCO, rect_iniciar)  # iniciar
#    pygame.draw.rect(pantalla, COLOR_BLANCO, rect_opciones)  # opciones
#    pygame.draw.rect(pantalla, COLOR_BLANCO, rect_puntuaciones)  # puntuaciones
#    pygame.draw.rect(pantalla, COLOR_BLANCO, rect_salir)  # salir


    pantalla.blit(iniciar_img, (105, 44))  
    pantalla.blit(opciones_img, (110, 177))  
    pantalla.blit(puntuaciones_img, (80, 275))    # Dibujar imágenes dentro de los rectángulos
    pantalla.blit(salir_img, (150, 355))  
    pantalla.blit(config_img, (10, 10))  

    pygame.display.flip()



