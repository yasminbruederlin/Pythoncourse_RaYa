import pygame  # import Pygame Paket
import os  # import Paket Betriebssystem
import sys  # import Paket System

# Verschiebe das Fenster an die gewünschten Koordinaten
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
# os.environ['SDL_VIDEO_CENTERED'] = '1'


def draw_text(display=None, xy=(0, 0), text='', colour=(255, 0, 0), size=16):
    """Funktion für das Zeichnen von Text auf die Pygame Leinwand."""
    font = pygame.font.SysFont(name="arial", size=size, bold=1)
    render_text = font.render(text, True, colour)
    display.blit(render_text, xy)


canvas_width = 200  # Breite der Leinwand
canvas_height = 200  # Höhe der Leinwand
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

    display.fill(BLACK)  # fülle die Leinwand mit schwarzer Farbe

    # zeichne Text
    draw_text(display, (10, 10), 'Text', WHITE, 12)
    draw_text(display, (10, 32), 'Text', WHITE, 14)
    draw_text(display, (10, 56), 'Text', WHITE, 16)
    draw_text(display, (10, 82), 'Text', GREEN, 18)
    draw_text(display, (10, 110), 'Text', BLUE, 24)
    draw_text(display, (10, 144), 'Text', RED, 36)

    pygame.display.update()  # aktualisiere die Leinwand

    # aktualisierung fps, warte solange damit die Framerate eingehalten wird
    fpsclock.tick(frames_per_second)

    # Titelleiste im Pygame Fenster
    pygame.display.set_caption(f'fps = {fpsclock.get_fps():.1f}')  # setze den Titel
