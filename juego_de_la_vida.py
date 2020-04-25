import pygame as pg
import numpy as np
import time

pg.init()

width, height = 800, 800
screen = pg.display.set_mode((height, width))
clock = pg.time.Clock()
fps = 24 # mas pequeño = mas lento el programa en detectar mouse y clicks

bg = 25, 25, 25
c_point = [(128, 128, 128),(255, 255, 255)]
screen.fill(bg)
run = True
pauseExect = False

nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

# Estructura de datos, almacena los estados. 1 = viva, 0 = muerta
gameState = np.zeros((nxC, nyC))

#Estado inicial
gameState[1, 1] = 1
gameState[2, 2] = 1
gameState[2, 3] = 1
gameState[1, 3] = 1
gameState[0, 3] = 1
#Fin estado inicial

while run:

	#No es secuencial los cambios, no depende de resultados anteriores
	newGameState = np.copy(gameState)

	screen.fill(bg)
	time.sleep(0.01)
	clock.tick(fps)

	for event in pg.event.get(): # User did something
		if event.type == pg.QUIT:
			run = False
		elif event.type == pg.KEYDOWN:
			pauseExect = not pauseExect

		mouseClick = pg.mouse.get_pressed()
		if sum(mouseClick) > 0:
			posX, posY = pg.mouse.get_pos()
			celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
			newGameState[celX][celY] = not mouseClick[2]

	for y in range(0, nxC):
		for x in range(0, nyC):

			if not pauseExect:

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
	pg.display.flip()

pg.quit()