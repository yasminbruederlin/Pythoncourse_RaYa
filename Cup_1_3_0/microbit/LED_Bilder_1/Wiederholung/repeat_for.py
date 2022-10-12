from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

for i in range(0, 4, 1):  # wiederhole 4 mal
    microbit.leds_update(DIAMOND)  # beschreibe die LEDs inklusive Update des Microbit
    sleep(0.25)  # pausiere für 0.25s
    microbit.leds_update(DIAMOND_SMALL)  # beschreibe die LEDs inklusive Update des Microbit
    sleep(0.25)  # pausiere für 0.25s

microbit.leds_clear_all_update()  # lösche alle LEDs und aktualisiere den Microbit

microbit.close()  # schliesse den Kommunikationskanal zum Microbit
