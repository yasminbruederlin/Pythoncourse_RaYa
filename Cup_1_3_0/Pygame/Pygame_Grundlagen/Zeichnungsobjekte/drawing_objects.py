import pygame  # import Pygame Paket
import os  # import Paket Betriebssystem
import sys  # import Paket System

# Verschiebe das Fenster an die gewünschten Koordinaten
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
# os.environ['SDL_VIDEO_CENTERED'] = '1'

canvas_width = 400  # Breite des Leinwand
canvas_height = 400  # Höhe des Leinwand
frames_per_second = 40  # Wiederholungen pro Sekunde

# Farbdefintionen
#            R    G    B
WHITE =     (255, 255, 255)
BLACK =     (0,     0,   0)
GRAY =      (100, 100, 100)
RED =       (255, 000,   0)
GREEN =     (  0, 255,   0)
BLUE =      (  0,   0, 255)

# Initialisierung
pygame.init()  # Initialisierung der Pygame Engine
fpsclock = pygame.time.Clock()  # Variable zur Speicherung der Bildwiderholung
display = pygame.display.set_mode((canvas_width, canvas_height), 0, 32)  # setze den Spielmodus

# Kontinuierliches Neuzeichnen der Leinwand und Auswertung der Events
while True:
    # Eventhandling Pygame
    for event in pygame.event.get():
        # beende Pygame mit der Maus oder der Taste Escape
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            print("exit")
            sys.exit()

    display.fill(WHITE)  # fülle die Leinwand mit schwarzer Farbe

    pygame.draw.circle(display, RED, (30, 30), 25, 0)  # Kreis ausgefüllt
    pygame.draw.circle(display, RED, (90, 30), 25, 1)  # Kreis mit Linienbreite 1

    pygame.draw.ellipse(display, GREEN, (10, 70, 80, 20), 0)  # Ellipse
    pygame.draw.ellipse(display, GREEN, (100, 70, 80, 20), 10)  # Ellipse mit Linienbreite 10

    pygame.draw.rect(display, BLUE, (10, 100, 80, 20), 0)  # Rechteck
    pygame.draw.rect(display, BLUE, (100, 100, 80, 20), 2)  # Rechteck mit Linienbreite 2

    pygame.draw.line(display, BLACK, (10, 150), (100, 150), 1)  # Linie der Breite 1
    pygame.draw.line(display, BLACK, (10, 160), (100, 200), 3)  # Linie der Breite 3
    pygame.draw.line(display, BLACK, (10, 200), (100, 170), 5)  # Linie der Breite 5

    pygame.display.update()  # aktualisiere die Leinwand

    # aktualisierung fps, warte solange damit die Framerate eingehalten wird
    fpsclock.tick(frames_per_second)

    # Titelleiste im Pygame Fenster
    pygame.display.set_caption(f'fps = {fpsclock.get_fps():.1f}')  # setze den Titel
