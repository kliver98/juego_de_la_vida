import pygame as pg
import numpy as np
import time

pg.init()

width, height = 700, 700
screen = pg.display.set_mode((height, width))

bg = 25, 25, 25
c_point = [(128, 128, 128),(255, 255, 255)]
screen.fill(bg)
run = True

nxC, nyC = 25, 25

dimCW = width / nxC
dimCH = height / nyC

# Estructura de datos, almacena los estados. 1 = viva, 0 = muerta
gameState = np.zeros((nxC, nyC))

#Pruebas, iniciando estados
#gameState[5, 3] = 1
#gameState[5, 4] = 1
#gameState[5, 5] = 1

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1
#Fin pruebas

while run:

	#No es secuencial los cambios, no depende de resultados anteriores
	newGameState = np.copy(gameState)

	screen.fill(bg)
	time.sleep(0.05)

	for y in range(0, nxC):
		for x in range(0, nyC):

			#Vecinos cercanos
			n_neigh = 	gameState[(x-1) % nxC, (y-1) % nyC] + \
						gameState[x 	% nxC, (y-1) % nyC] + \
						gameState[(x+1) % nxC, (y-1) % nyC] + \
						gameState[(x-1) % nxC, y 	 % nyC] + \
						gameState[(x+1) % nxC, y 	 % nyC] + \
						gameState[(x-1) % nxC, (y+1) % nyC] + \
						gameState[x 	% nxC, (y+1) % nyC] + \
						gameState[(x+1) % nxC, (y+1) % nyC]

			#Regla 1: revive
			if gameState[x,y] == 0 and (n_neigh == 3):
				newGameState[x,y] = 1

			#Regla 2: muere
			elif gameState[x,y] == 1 and (n_neigh <2 or n_neigh>3):
				newGameState[x,y] = 0

			poly = [((x) * dimCW, y * dimCH),
					((x+1) * dimCW, y * dimCH),
					((x+1) * dimCW, (y+1) * dimCH),
					(x * dimCW, (y+1) * dimCH)]

			if newGameState[x,y] == 0:
				pg.draw.polygon(screen, c_point[0], poly, 1)
			else:
				pg.draw.polygon(screen, c_point[1], poly, 0)

	gameState = np.copy(newGameState)
	for event in pg.event.get(): # User did something
		if event.type == pg.QUIT:
			run = False
	pg.display.flip()

pg.quit()