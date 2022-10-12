# Pygame und micro:bit
Durch die Verbindung der grafischen Pygame Bibliothek mit dem Einplatinencomputer micro:bit
entstehen interessante Interaktionsmöglichkeiten.
Durch die Modularisierung des micro:bit Kommunikationstreibers kann dieser durch einen
zusätzlichen Modulimport am Skriptanfang in die Pygame-Struktur integriert werden `from microbit_wings import *`.

Wie im Kapitel micro:bit ausführlich erläutert, ist die Schnittstelle zu öffnen `microbit.open()`,
bevor mittels `microbit.update()` die kontinuirliche Kommunikation zum micro:bit ausgeführt werden kann.  

Das Eventhandling, welches im Zusammenhang mit dem micro:bit steht, erfolgt am  im Anschluss an das Eventhandling
von Pygame.
````python
if microbit.button_event_a:  # Taste a
    print('Taste a gedrückt')
elif microbit.button_event_b:  # Taste b
    print('Taste b gedrückt')
...
````

