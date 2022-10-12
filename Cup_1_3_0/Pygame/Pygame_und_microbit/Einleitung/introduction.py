import pygame  # import Pygame Paket
from microbit_wings import *  # importiere die benötigten Bibliotheken für den micro:bit
import os, sys  # importiere Systembibliotheken

# Verschiebe das Fenster an die gewünschten Koordinaten
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
# os.environ['SDL_VIDEO_CENTERED'] = '1'

# Farbdefintionen
#            R    G    B
WHITE =     (255, 255, 255)
BLACK =     (0,     0,   0)

window_width = 300  # Breite des Spielfeldes
window_height = 300  # Höhe des Spielfeldes
frames_per_second = 40  # Wiederholungsgeschwindigket in Frames per Second

pygame.init()
fpsclock = pygame.time.Clock()
display = pygame.display.set_mode((window_width, window_height), 0, 32)

microbit.open()  # öffne den Kommunikationskanal zum Microbit

while True:
    # Eventhandling Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            microbit.leds_clear_all_update()
            microbit.close()
            pygame.quit()
            print("exit")
            sys.exit()

    # Eventhandling Microbit
    if microbit.button_event_a:  # Taste a
        print('Taste a gedrückt')
    elif microbit.button_event_b:  # Taste b
        print('Taste b gedrückt')

    display.fill(BLACK)  # fülle die Leinwand mit schwarzer Farbe

    pygame.display.update()  # aktualisiere die Leinwand
    microbit.update()  # aktualisiere den Microbit

    # aktualisierung fps, warte solange damit die Framerate eingehalten wird
    fpsclock.tick(frames_per_second)

    # Titelleiste im Pygame Fenster
    pygame.display.set_caption(f'fps = {fpsclock.get_fps():.1f}')  # setze den Titel

    # Titelleiste im Pygame Fenster
    pygame.display.set_caption(f'fps = {fpsclock.get_fps():.1f}')  # setze den Titel
