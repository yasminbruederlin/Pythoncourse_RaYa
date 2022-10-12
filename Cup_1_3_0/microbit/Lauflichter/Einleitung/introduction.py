from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

microbit.leds_clear_all()  # lösche alle Leuchtdioden

microbit.leds[0][0] = True  # setze Leuchtdiode in Zeile 0, Spalte 0

microbit.update()  # aktualisiere den Microbit

sleep(0.5)  # warte

microbit.leds[2][3] = True  # setze Leuchtdiode in Zeile 2, Spalte 3

microbit.update()  # aktualisiere den Microbit

sleep(0.5)  # warte

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit

microbit.close()  # schliesse den Kommunikationskanal zum Microbit