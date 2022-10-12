# Sound
[Onlinehilfe Pygame Mixer (Sound)](https://www.pygame.org/docs/ref/mixer.html)  

Das Mixermodul lädt Sounddateien aus dem Dateisystem und spielt diese ab.  
Hinweis: Das Modul kann nur Dateien im WAV Format verarbeiten!

````python
pygame.mixer.init()  # initialisiere den Soundmixer
sound_rooster = pygame.mixer.Sound("sound/rooster.wav")  # rooster.wav
sound_rooster.set_volume(1.0)  # setze die Lautstärke
sound_rooster.play()  # spiele die Sounddatei 1x
sound_rooster.play(loops=-1)  # spiele die Sounddatei in einer Dauerschlaufe
sound_rooster.stop()  # stoppe die Sounddatei
````