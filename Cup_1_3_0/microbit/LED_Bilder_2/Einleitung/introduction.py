from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

# bilde eine Liste aus 5 Bibliotheksbildern
images = [SMILE, HAPPY, CONFUSED, SAD, ANGRY]

# images.reverse()  # drehe die Reihenfolge der Listelemente

print('Anzahl Elemente in der Liste: ', len(images))

for i in range(0, len(images), 1):
    microbit.leds_update(images[i])  # beschreibe die LEDs inklusive Update des Microbit
    sleep(0.5)  # pausiere für 0.5s

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit
sleep(1.0)  # pausiere für 1.0s

for image_to_show in images:  # iteriere über jedes Listenelement
    microbit.leds_update(image_to_show)  # beschreibe die LEDs inklusive Update des Microbit
    sleep(0.5)  # pausiere für 0.25s

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit

microbit.close()  # schliesse den Kommunikationskanal zum Microbit
