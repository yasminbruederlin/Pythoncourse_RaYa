import pygame  # Pygame Modul
from random import random  # Zufallszahlen
import os  # import Paket Betriebssystem
import sys  # import Paket System

# Farbdefintionen
#            R    G    B
WHITE =     (255, 255, 255)
GRAY =      (100, 100, 100)

# Verschiebe das Fenster an die gewünschten Koordinaten
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
os.environ['SDL_VIDEO_CENTERED'] = '1'

canvas_width = 800  # Breite der Leinwand
canvas_height = 600  # Höhe der Leinwand
frames_per_second = 40  # Wiederholungsgeschwindigket in Frames per Second

# Bildintegration
car_width = 120  # Breite des Autos in Pixel
car_heigth = 210  # Höhe des Autos in Pixel
car_skin = pygame.image.load('img/car_skin_120_210.jpg')
grass_width = 100  # Breite des Seitenrandes in Pixel
grass_height = 600  # Höhe des Seitenrandes in Pixel
grass_boundary = pygame.image.load('img/grass_boundary_100_600.jpg')

car_x_centre = int(canvas_width / 2 - car_width / 2)  # Zentrum des Autobildes auf der x Achse

# Variablen zur Steuerung des eigenen Autos
my_car_position_x = 0  # Position auf der x Achse des Autos. Mögliche Positionen (-2, -1, 0, 1 , 2)
my_car_x = my_car_position_x * car_width + car_x_centre  # Position in Pixel auf der x Achse
my_car_y = canvas_height - car_heigth - 5  # Position in Pixel auf der y Achse

# Initialisierung Pygame
pygame.init()  # Initialisierung Pygame
display = pygame.display.set_mode((canvas_width, canvas_height), 0, 32)  # erstelle eine Anzeige
fpsclock = pygame.time.Clock()  # Initialisierung des Framerateclocks

while True:
    # Bildaufbau, grafische Gestaltung
    display.fill(GRAY)  # zeichne den Hintergrund
    display.blit(grass_boundary, (0, 0))  # zeichne den linken Seitenrand mit Gras
    # zeichne den rechten Seitenrand mit Gras
    display.blit(grass_boundary, ((canvas_width - grass_width), 0))

    # bestimme die Koordinaten für das eigene Auto
    my_car_x = my_car_position_x * car_width + car_x_centre
    display.blit(car_skin, (my_car_x, my_car_y))  # zeichne das eigene Auto

    # Eventhandling Keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            print("exit")
            sys.exit()

        # speichere das Display in car_race.png
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            print('speichere Display nach img/car_race.png')
            pygame.image.save(display, 'img/car_race.png')

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # bewege das Auto nach links
                if my_car_position_x > -2:
                    my_car_position_x -= 1
            elif event.key == pygame.K_RIGHT:  # bewege das Auto nach rechts
                if my_car_position_x < 2:
                    my_car_position_x += 1

    pygame.display.update()  # aktualisiere die Leinwand

    # Aktualisierung fps
    fpsclock.tick(frames_per_second)
    pygame.display.set_caption(f'Autorennen | fps: {fpsclock.get_fps():.1f}')
