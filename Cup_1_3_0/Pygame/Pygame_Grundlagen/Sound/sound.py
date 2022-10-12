import pygame  # import Pygame Paket
import os  # import Paket Betriebssystem
import sys  # import Paket System

# Verschiebe das Fenster an die gewünschten Koordinaten
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
# os.environ['SDL_VIDEO_CENTERED'] = '1'

canvas_width = 100  # Breite des Leinwand
canvas_height = 100  # Höhe des Leinwand
frames_per_second = 40  # Wiederholungen pro Sekunde

# Farbdefintionen
#            R    G    B
WHITE =     (255, 255, 255)
BLACK =     (0,     0,   0)

# Soundintegration
pygame.mixer.init()  # initialisiere den Soundmixer
sound_rooster = pygame.mixer.Sound("sound/rooster.wav")  # rooster.wav
sound_rooster.set_volume(1.0)  # setze die Lautstärke

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

        # Auswertung der Keyboardpfeiltasten
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # spiele die Sounddatei 1x
                sound_rooster.play()
                print('spiele die Sounddatei 1x')

            elif event.key == pygame.K_f:  # spiele die Sounddatei in einer Dauerschlaufe
                sound_rooster.play(loops=-1)
                print('spiele die Sounddatei in einer Dauerschlaufe')

            elif event.key == pygame.K_s:  # stoppe die Sounddatei
                sound_rooster.stop()
                print('stoppe die Sounddatei')

            elif event.key == pygame.K_DOWN:  # senke die Lautstärke
                volume = sound_rooster.get_volume() - 0.1
                if volume < 0.0:
                    volume = 0.0
                sound_rooster.set_volume(volume)
                print(f'senke die Lautstärke auf {volume:1.01f}')

            elif event.key == pygame.K_UP:  # erhöhe die Lautstärke
                volume = sound_rooster.get_volume() + 0.1
                if volume > 1.0:
                    volume = 1.0
                sound_rooster.set_volume(volume)
                print(f'erhöhe die Lautstärke auf {volume:1.01f}')

    display.fill(BLACK)  # fülle die Leinwand mit schwarzer Farbe

    pygame.display.update()  # aktualisiere die Leinwand

    # aktualisierung fps, warte solange damit die Framerate eingehalten wird
    fpsclock.tick(frames_per_second)

    # Titelleiste im Pygame Fenster
    pygame.display.set_caption(f'fps = {fpsclock.get_fps():.1f}')  # setze den Titel
