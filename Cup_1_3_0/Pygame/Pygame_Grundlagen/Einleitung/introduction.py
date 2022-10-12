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

mouse_x = 0  # Variable in welcher die x-Koordinate der Mausbewegung gespeichert wird
mouse_y = 0  # Variable in welcher die y-Koordinate der Mausbewegung gespeichert wird
mouse_x_click = 0  # Variable in welcher die x-Koordinate des Mausklicks gespeichert wird
mouse_y_click = 0  # Variable in welcher die y-Koordinate des Mausklicks gespeichert wird

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

        # Event nach einer Mausbewegung
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos  # Erfassung der Mauskoordinaten. Die Rückgabe erfolgt in der Form einer Liste

        # Event nach einem Mausklick
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_click, mouse_y_click = event.pos  # Erfassung der Mauskoordinaten. Die Rückgabe erfolgt in der Form einer Liste
            print(f'click x = {mouse_x_click:03d} y = {mouse_y_click:03d}')

    display.fill(BLACK)  # fülle die Leinwand mit schwarzer Farbe

    pygame.draw.circle(display, RED, (mouse_x, mouse_y), 20, 0)  # zeichne einen roten Kreis an den Mauskoordinaten

    pygame.display.update()  # aktualisiere die Leinwand

    # aktualisierung fps, warte solange damit die Framerate eingehalten wird
    fpsclock.tick(frames_per_second)

    # Titelleiste im Pygame Fenster
    pygame.display.set_caption(f'x = {mouse_x:03d} y = {mouse_y:03d} | fps = {fpsclock.get_fps():.1f}')  # setze den Titel
