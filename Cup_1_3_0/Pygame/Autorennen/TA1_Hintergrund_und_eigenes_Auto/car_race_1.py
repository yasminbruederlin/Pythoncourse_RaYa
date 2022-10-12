import pygame  # import Pygame Paket
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

# Initialisierung Pygame
pygame.init()  # Initialisierung Pygame
display = pygame.display.set_mode((canvas_width, canvas_height), 0, 32)  # erstelle eine Anzeige
fpsclock = pygame.time.Clock()  # Initialisierung des Framerateclocks

while True:
    # Bildaufbau, grafische Gestaltung
    display.fill(WHITE)  # zeichne den Hintergrund

    # Eventhandling Keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            print("exit")
            sys.exit()

    pygame.display.update()  # aktualisiere die Leinwand

    # Aktualisierung fps
    fpsclock.tick(frames_per_second)
    pygame.display.set_caption(f'Autorennen | fps: {fpsclock.get_fps():.1f}')