from cgitb import text
from tkinter import font
from turtle import title
import pygame
from pygame.locals import *

# Asignamos los colores principales
BLACK = (0,0,0)
WHITE = (255,255,255)

# Guardamos variables con el tamaño de la pantalla
WIDTH = 400
HEIGHT = 500

# Esta lista contendrá los elementos a renderizar
elements = []

# Esta lista contendrá las fuentes del programa
fonts = []

# Función que muestra el logotipo y autor
def intro(fonts):
    # Le indicamos que la variable ya existe
    global elements

    # Creamos y añadimos a la lista de renderizado
    # Además Creamos un rectángulo para poder centrarlo verticalmente en la pantalla
    title = fonts[0].render("Calculadora",True,BLACK)
    title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2))

    author = fonts[1].render("Mario Perdiguero",True,BLACK)
    author_rect = author.get_rect(center=(WIDTH/2, HEIGHT/2+40))


    elements.append([title,title_rect])
    elements.append([author,author_rect])

# Función Principal
def main():
    # Indicamos que la variable ya existe
    global fonts

    # Inicializar el módulo de pygame
    pygame.init()

    # Definimos las fuentes
    H1 = pygame.font.Font("fonts/Archivo-Black.ttf", 48)
    H2 = pygame.font.Font("fonts/Archivo-Light.ttf", 24)
    # Añadimos las fuentes a la lista
    fonts.append(H1)
    fonts.append(H2)

    # Cargar y establecer el icono de la aplicación
    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)
    
    # Establecer el título de la ventana
    pygame.display.set_caption("Calculadora")

    # Crear la superficie sobre la pantalla
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    # Definir una variable para controlar el ciclo principal
    running = True

    intro(fonts)

    # Ciclo Principal
    while running:
        # Manejar los eventos, obtenerlos desde una lista
        for event in pygame.event.get():
            # Si el evento es QUIT, cerraremos el programa
            if event.type == pygame.QUIT:
                # Cambiamos el valor de la variable para salir
                running = False
        
        # Pintamos la pantalla de blanco
        screen.fill((200,200,200))

        # Recorremos la lista de elementos renderizables
        for element in elements:
            # Por cada elemento:
            #   - Obtenemos el elemento a renderizar
            #   - Obtenemos la posición a renderizar
            screen.blit(element[0],element[1])

        # Actualizamos la pantalla  
        pygame.display.update()

# Ejecutamos la función principal solo si este código se ha ejecutado principalmente
# Si importamos como un módulo nada ocurrirá
if __name__ == "__main__":
    # Llamamos a la función principal
    main()