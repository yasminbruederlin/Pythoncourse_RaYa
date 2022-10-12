from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

if microbit.button_a:  # ist die Taste a gedrückt?
    print('=> Taste a gedrückt <=')

if microbit.button_b:  # ist die Taste b gedrückt?
    print('=> Taste b gedrückt <=')

microbit.close()  # schliesse den Kommunikationskanal zum Microbit
