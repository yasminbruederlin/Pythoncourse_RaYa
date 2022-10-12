from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

if microbit.button_a and microbit.button_b:  # sind die Tasten a und b gedrückt?
    print('=> Taste a und b gedrückt <=')
elif microbit.button_a:  # ist die Taste a gedrückt?
    print('=> Taste a gedrückt <=')
elif microbit.button_b:  # ist die Taste b gedrückt?
    print('=> Taste b gedrückt <=')
else:
    print('=> keine Taste gedrückt <=')

microbit.close()  # schliesse den Kommunikationskanal zum Microbit
