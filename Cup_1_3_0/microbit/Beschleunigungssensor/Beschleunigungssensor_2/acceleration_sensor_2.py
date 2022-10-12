from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

column = 0  # Variable für die Zeile
while not microbit.button_a and not microbit.button_b:  # solange Taste a oder Taste b nicht gedrückt
    microbit.update()  # aktualisiere den Microbit

    print(f'x = {microbit.acc_x:.02f}')  # schreibe die aktuellen Werte der x-Beschleunigung in das Terminal

    if microbit.acc_x > 0.5:  # x > 0.5
        column = 4

    elif (microbit.acc_x <= 0.5) and (microbit.acc_x > 0.25):  # (x <= 0.5) and (x > 0.25)
        column = 3

    elif (microbit.acc_x <= 0.25) and (microbit.acc_x > -0.25):  # (x <= 0.25) and (x > -0.25)
        column = 2

    elif (microbit.acc_x <= -0.25) and (microbit.acc_x > -0.5):  # (x <= -0.25) and (x > -0.5)
        column = 1

    elif microbit.acc_x <= -0.5:  # x <= -0.5
        column = 0

    microbit.leds_clear_all()  # lösche alle Leuchtdioden
    microbit.leds[2][column] = True  # setze Leuchtdiode in Zeile 2, Spalte 4

    sleep(0.25)  # warte

microbit.close()  # schliesse den Kommunikationskanal zum Microbit

print('Programmende')