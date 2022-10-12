from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

print('Beschleunigungssensor')

while not microbit.button_a or not microbit.button_b:  # solange Taste a oder Taste b nicht gedrückt
    microbit.update()  # aktualisiere den Microbit

    # schreibe die aktuellen Werte in das Terminal
    print(f'x = {microbit.acc_x:.02f} | y = {microbit.acc_y:.02f} | z = {microbit.acc_z:.02f}')

    sleep(0.25)  # warte

microbit.close()  # schliesse den Kommunikationskanal zum Microbit

print('Programmende')
