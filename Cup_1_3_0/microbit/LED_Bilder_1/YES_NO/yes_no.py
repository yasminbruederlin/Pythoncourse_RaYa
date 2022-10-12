from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

microbit.leds_update(YES)  # beschreibe die LEDs inklusive Update des Microbit

sleep(1)  # pausiere für 1s

microbit.leds_update(NO)  # beschreibe die LEDs inklusive Update des Microbit

sleep(1)  # pausiere für 1s

microbit.close()  # schliesse den Kommunikationskanal zum Microbit
