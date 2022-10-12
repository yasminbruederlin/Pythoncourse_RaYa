import pygame  # Pygame Modul
from microbit_wings import *  # micro:bit Kommunikationstreiber
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


def draw_text(display=None, xy=(0, 0), text='', colour=(255, 0, 0), size=16):
    """Funktion für das Zeichnen von Text auf die Pygame Leinwand."""
    font = pygame.font.SysFont(name="arial", size=size, bold=1)
    render_text = font.render(text, True, colour)
    display.blit(render_text, xy)


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

car_x_centre = round(canvas_width / 2 - car_width / 2)  # Zentrum des Autobildes auf der x Achse

# Variablen zur Steuerung des eigenen Autos
my_car_position_x = 0  # Position auf der x Achse des Autos. Mögliche Positionen (-2, -1, 0, 1 , 2)
my_car_x = my_car_position_x * car_width + car_x_centre  # Position in Pixel auf der x Achse
my_car_y = canvas_height - car_heigth - 5  # Position in Pixel auf der y Achse

# Variablen des entgegenkommenden Fahrzeuges
random_position = round(random() * 4) - 2  # Zufallszahl für die Bestimmung der Position (-2, -1, 0, 1 , 2)
random_position_old = random_position  # Hilfsvariable zur Optimierung der Postionierung
car_position_x = random_position  # Position auf der x Achse des Autos. Mögliche Positionen (-2, -1, 0, 1 , 2)
car_x = car_position_x * car_width + car_x_centre  # Position in Pixel auf der x Achse
car_y = -car_heigth  # Position in Pixel auf der y Achse
car_velocity = 15  # Geschwindigkeit des zu überholenden Fahrzeuges

score = 0  # Punktestand
car_drive_enable = False  # Variable für die Freigabe des zu überholenden Autos

# Initialisierung Pygame und micro:bit
pygame.init()  # Initialisierung Pygame
display = pygame.display.set_mode((canvas_width, canvas_height), 0, 32)  # erstelle eine Anzeige
fpsclock = pygame.time.Clock()  # Initialisierung des Framerateclocks
microbit.open()  # öffne den Kommunikationsport zum micro:bit

while True:
    # Bildaufbau, grafische Gestaltung
    display.fill(GRAY)  # zeichne den Hintergrund
    display.blit(grass_boundary, (0, 0))  # zeichne den linken Seitenrand mit Gras
    # zeichne den rechten Seitenrand mit Gras
    display.blit(grass_boundary, ((canvas_width - grass_width), 0))

    # bestimme die Koordinaten für das eigene Auto
    my_car_x = my_car_position_x * car_width + car_x_centre
    display.blit(car_skin, (my_car_x, my_car_y))  # zeichne das eigene Auto

    # bestimme die Koordinaten für das überholende Fahrzeug
    if car_drive_enable:  # ist das zu überholenden Auto freigegeben
        car_y += car_velocity  # Neuberechnung der y Koordinate => Bewegungseffekt
    else:
        draw_text(display, (115, 50), 'STARTE MIT [SPACE] DAS SPIEL', WHITE, 36)

    car_x = car_position_x * car_width + car_x_centre
    display.blit(car_skin, (car_x, car_y))  # zeichne das überholende Auto

    # aktueller Spielstand
    draw_text(display, (740, 30), f'{score:3d}', WHITE, 36)

    # Detektion Crash
    car_crash = (my_car_position_x == car_position_x) and (car_y >= (my_car_y - car_heigth))

    # Falls das zu überholende Fahrzeug am unteren Bildrand angelangt ist, wird die x Position
    # und die y Position neu bestimmt => nächstes zu überholendes Fahrzeug
    if car_y > canvas_height or car_crash:
        while random_position == random_position_old:  # solange die neue Position der alten entspricht
            random_position_temp = round(random() * 2)  # temporäre Variable
            if my_car_position_x == -2:  # Position -2 => linker Rand
                random_position = -2 + random_position_temp  # Berechnung der neuen Position
            elif (my_car_position_x >= -1) and (my_car_position_x <= 1):  # Position -1, 0, 1
                random_position = my_car_position_x + random_position_temp - 1  # Berechnung der neuen Position
            elif my_car_position_x == 2:  # Position 2 => rechter Rand
                random_position = 2 - random_position_temp  # Berechnung der neuen Position

        # Die neue und die alte Position werden gleichgesetzt.
        # Im nächsten Iterationszyklus erfolgt die Auswertung
        random_position_old = random_position

        car_position_x = random_position
        car_y = -car_heigth
        # Punktezähler
        if not car_crash:
            score += 1  # erhöhe den Punktestand
        else:
            car_drive_enable = False  # stoppe die Fahrt des zu überholenden Autos

    # Eventhandling Keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            microbit.close()  # schliessen den Kommunikationsport zum micro:bit
            pygame.quit()
            print("exit")
            sys.exit()

        # speichere das Display in car_race.png
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            print('speichere Display nach img/car_race.png')
            pygame.image.save(display, 'img/car_race.png')

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # starte das Spiel
                car_drive_enable = True  # starte die zu überholenden Autos
                score = 0  # Reset des Punktezählers
            elif event.key == pygame.K_LEFT:  # bewege das Auto nach links
                if my_car_position_x > -2:
                    my_car_position_x -= 1
            elif event.key == pygame.K_RIGHT:  # bewege das Auto nach rechts
                if my_car_position_x < 2:
                    my_car_position_x += 1

    # Eventhandling micro:bit
    if microbit.button_event_a:  # bewege das Auto nach links
        if my_car_position_x > -2:
            my_car_position_x -= 1
    elif microbit.button_event_b:  # bewege das Auto nach rechts
        if my_car_position_x < 2:
            my_car_position_x += 1

    pygame.display.update()  # aktualisiere die Leinwand
    microbit.update()

    # Aktualisierung fps
    fpsclock.tick(frames_per_second)
    pygame.display.set_caption(f'Autorennen | fps: {fpsclock.get_fps():.1f}')
