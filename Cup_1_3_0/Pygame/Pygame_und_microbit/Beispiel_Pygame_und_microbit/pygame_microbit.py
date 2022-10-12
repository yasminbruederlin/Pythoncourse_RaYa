import pygame  # import Pygame Paket
from microbit_wings import *  # importiere die benötigten Bibliotheken für den micro:bit
import os  # import Paket Betriebssystem
import sys  # import Paket System

# Verschiebe das Fenster an die gewünschten Koordinaten
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
# os.environ['SDL_VIDEO_CENTERED'] = '1'

# Farbdefintionen
#            R    G    B
WHITE =     (255, 255, 255)
BLACK =     (0,     0,   0)
GRAY =      (100, 100, 100)
RED =       (255, 000,   0)
GREEN =     (  0, 255,   0)
BLUE =      (  0,   0, 255)


def draw_text(display=None, xy=(0, 0), text='', colour=(255, 0, 0), size=16):
    """Funktion für das Zeichnen von Text auf die Pygame Leinwand."""
    font = pygame.font.SysFont(name="arial", size=size, bold=1)
    render_text = font.render(text, True, colour)
    display.blit(render_text, xy)


window_width = 300  # Breite des Spielfeldes
window_height = 300  # Höhe des Spielfeldes
frames_per_second = 40  # Wiederholungsgeschwindigket in Frames per Second

row = 2
column = 2

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
        # Auswertung der Keyboardpfeiltasten
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                column -= 1
                if column < 0:
                    column = 0
            elif event.key == pygame.K_RIGHT:
                column += 1
                if column > 4:
                    column = 4
            elif event.key == pygame.K_DOWN:
                row += 1
                if row > 4:
                    row = 4
            elif event.key == pygame.K_UP:
                row -= 1
                if row < 0:
                    row = 0

    display.fill(BLACK)  # fülle die Leinwand mit schwarzer Farbe

    # zeichne das 5 x 5 Gitter
    for i in range(60, 300, 60):
        pygame.draw.line(display, GRAY, (0, i), (300, i), 1)
        pygame.draw.line(display, GRAY, (i, 0), (i, 300), 1)

    # zeichne einen roten Kreis auf die aktulle Position
    pygame.draw.circle(display, RED, ((column * 60) + 30, (row * 60) + 30), 25, 0)

    # zeichne Text mit der aktuellen Zeile und Spalte
    draw_text(display, (10, 0), f'Zeile  = {row:d}', RED)
    draw_text(display, (10, 20), f'Spalte  = {column:d}', RED)

    pygame.display.update()  # aktualisiere die Leinwand

    # Eventhandling Microbit
    if microbit.button_event_a and (abs(microbit.acc_y) < 0.25):  # Taste a micro:bit liegend
        column -= 1
        if column < 0:
            column = 0

    elif microbit.button_event_b and (abs(microbit.acc_y) < 0.25):  # Taste b micro:bit liegend
        column += 1
        if column > 4:
            column = 4

    elif microbit.button_event_a and (abs(microbit.acc_y) > 0.50):  # Taste a micro:bit geneigt
        row += 1
        if row > 4:
            row = 4

    elif microbit.button_event_b and (abs(microbit.acc_y) > 0.50):  # Taste b micro:bit geneigt
        row -= 1
        if row < 0:
            row = 0

    # Update Microbit
    microbit.update()  # aktualisiere den Microbit
    microbit.leds_clear_all()  # lösche alle Leuchtdioden
    microbit.leds[row][column] = True  # setze Leuchtdiode in Zeile x, Spalte y

    # Aktualisierung fps
    fpsclock.tick(frames_per_second)  # warte solange, damit die Frameraet eingehalten wird

    # Titelleiste im Pygame Fenster
    pygame.display.set_caption(f'fps = {fpsclock.get_fps():.1f}')  # setze den Titel
