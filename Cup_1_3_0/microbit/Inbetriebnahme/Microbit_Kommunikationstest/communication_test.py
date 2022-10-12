from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

microbit.leds_update(HAPPY)  # beschreibe die LEDs inklusive Update des Microbit

microbit.close()  # schliesse den Kommunikationskanal zum Microbit