import pygame
import sys
import random


# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana y el tamaño de los píxeles
ventana_ancho = 800
ventana_alto = 800
pixel_size = 5



tamanio = int(ventana_alto/pixel_size)

def condicionVida(sum , _tablero, i, j):
    if  sum == 3 :
        _tablero[i][j] = 1
    elif sum < 2 or sum >= 4:
        _tablero[i][j] = 0


def actualizar_tablero(tablero): 
    tablero_aux =   [[0]*tamanio for _ in range(tamanio)]

    for i in range(tamanio):
        for j in range(tamanio):
            tablero_aux[i][j] = tablero[i][j] 

    for i in range(tamanio):
        for j in range(tamanio):
            if i == 0: 
                if j == 0: 
                    sum =  tablero[i][j+1] + tablero[i+1][j+1] + tablero[i+1][j] 
                    condicionVida(sum, tablero_aux, i, j)

                elif j > 0 and j < (tamanio - 1) : 
                    sum =  tablero[i][j-1] + tablero[i+1][j-1] + tablero[i+1][j]+ tablero[i][j+1] + tablero[i+1][j+1] 
                    condicionVida(sum, tablero_aux, i, j)

                else :
                    sum =  tablero[i][j-1] + tablero[i+1][j-1] + tablero[i+1][j] 
                    condicionVida(sum, tablero_aux, i, j)

            elif i > 0 and i < (tamanio -1) :
                if j == 0: 
                    sum =  tablero[i-1][j] + tablero[i-1][j+1] + tablero[i][j+1]+ tablero[i+1][j] + tablero[i+1][j+1]  
                    condicionVida(sum, tablero_aux, i, j)

                elif j > 0 and j < (tamanio - 1) : 
                    sum =  tablero[i-1][j-1] + tablero[i-1][j] + tablero[i-1][j+1]+ tablero[i][j-1] + tablero[i][j+1] +tablero[i+1][j-1] +tablero[i+1][j] +tablero[i+1][j+1] 
                    condicionVida(sum, tablero_aux, i, j)
                else :
                    sum =  tablero[i-1][j] + tablero[i-1][j-1] + tablero[i][j-1]+ tablero[i+1][j-1] + tablero[i+1][j]  
                    condicionVida(sum, tablero_aux, i, j)
            else :
                if j == 0:
                    sum =  tablero[i-1][j] + tablero[i-1][j+1] + tablero[i][j+1] 
                    condicionVida(sum, tablero_aux, i, j)  
                elif j > 0 and j < (tamanio - 1) :
                    sum =  tablero[i][j-1] + tablero[i-1][j-1] + tablero[i-1][j]+ tablero[i-1][j+1] + tablero[i][j+1] 
                    condicionVida(sum, tablero_aux, i, j)
                else:
                    sum =  tablero[i][j-1] + tablero[i-1][j-1] + tablero[i-1][j] 
                    condicionVida(sum, tablero_aux, i, j) 
    return tablero_aux




# Configurar la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Dibujo en Píxeles")

# Función para dibujar el dibujo en la ventana
def dibujar_dibujo(surface, dibujo):
    for i in range(len(dibujo)):
        for j in range(len(dibujo[0])):
            color = (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)) if dibujo[i][j] == 1 else pygame.Color("white") 
            pygame.draw.rect(surface, color, (j * pixel_size, i * pixel_size, pixel_size, pixel_size))

# Bucle principal del juego

tablero_final = [[random.randint(0, 1) for _ in range(tamanio)] for _ in range(tamanio)]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el dibujo en la ventana
    ventana.fill((255, 255, 255)) 
    dibujar_dibujo(ventana, tablero_final)
    
    tablero_final = actualizar_tablero(tablero_final)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)

