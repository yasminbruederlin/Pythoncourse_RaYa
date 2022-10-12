from microbit_wings import *  # importiere die benötigten Bibliotheken

print('Programmstart')  # Ausgabe an das Terminal

microbit.open()  # öffne den Kommunikationskanal zum Microbit

counter = 0  # erstelle eine Zählvariable für die Anzahl der Tastenbetätigungen

while counter < 10:  # solange die Variable kleiner 10
    microbit.update()  # aktualisiere den Microbit
    if microbit.button_a:
        counter = counter - 1  # subtrahiere zum aktuellen Zählerwert 1
        print(f'=> Taste a gedrückt <= | counter = {counter:d}')
        sleep(0.25)  # warte damit keine Mehrfachbetätigungen erfasst werden

    elif microbit.button_b:
        counter = counter + 1  # addiere zum aktuellen Zählerwert 1
        print(f'=> Taste b gedrückt <= | counter = {counter:d}')
        sleep(0.25)  # warte damit keine Mehrfachbetätigungen erfasst werden

microbit.close()  # schliesse den Kommunikationskanal zum Microbit

print('Programmende')  # Ausgabe an das Terminal
