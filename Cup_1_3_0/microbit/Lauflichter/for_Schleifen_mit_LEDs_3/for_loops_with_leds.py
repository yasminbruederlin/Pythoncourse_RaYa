from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

microbit.leds_clear_all()  # lösche alle Leuchtdioden

for i in range(0, 5, 1):
    microbit.leds[2][4-i] = True  # setze Leuchtdiode in Zeile 0, Spalte i
    microbit.update()  # aktualisiere den Microbit
    sleep(0.5)  # warte

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit
sleep(0.5)  # warte

for i in range(0, 5, 1):
    microbit.leds[4-i][1] = True  # setze Leuchtdiode in Zeile 0, Spalte i
    microbit.leds[4-i][3] = True  # setze Leuchtdiode in Zeile 0, Spalte i
    microbit.update()  # aktualisiere den Microbit
    sleep(0.5)  # warte

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit

microbit.close()  # schliesse den Kommunikationskanal zum Microbit
