from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

microbit.leds_clear_all()  # lösche alle Leuchtdioden

for i in range(4, -1, -1):
    microbit.leds[0][i] = True  # setze Leuchtdiode in Zeile 0, Spalte i
    microbit.update()  # aktualisiere den Microbit
    sleep(0.5)  # warte

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit
sleep(0.5)  # warte

for i in range(4, -1, -1):
    microbit.leds[i][0] = True  # setze Leuchtdiode in Zeile i, Spalte 0
    microbit.update()  # aktualisiere den Microbit
    sleep(0.5)  # warte

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit
sleep(0.5)  # warte

for i in range(4, -1, -1):
    microbit.leds[i][i] = True  # setze Leuchtdiode in Zeile i, Spalte 0
    microbit.update()  # aktualisiere den Microbit
    sleep(0.5)  # warte

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit

microbit.close()  # schliesse den Kommunikationskanal zum Microbit