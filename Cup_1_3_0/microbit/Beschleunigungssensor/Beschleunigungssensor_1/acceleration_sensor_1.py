from microbit_wings import *  # importiere die benötigten Bibliotheken

microbit.open()  # öffne den Kommunikationskanal zum Microbit

while not microbit.button_a and not microbit.button_b:  # solange Taste a oder Taste b nicht gedrückt
    microbit.update()  # aktualisiere den Microbit

    print(f'x = {microbit.acc_x:.02f}')  # schreibe die aktuellen Werte der x-Beschleunigung in das Terminal

    microbit.leds_clear_all()  # lösche alle Leuchtdioden
    if microbit.acc_x > 0.5:  # x > 0.5
        microbit.leds[2][4] = True  # setze Leuchtdiode in Zeile 2, Spalte 0

    elif (microbit.acc_x <= 0.5) and (microbit.acc_x > 0.25):  # (x <= 0.5) and (x > 0.25)
        microbit.leds[2][3] = True  # setze Leuchtdiode in Zeile 2, Spalte 1

    elif (microbit.acc_x <= 0.25) and (microbit.acc_x > -0.25):  # (x <= 0.25) and (x > -0.25)
        microbit.leds[2][2] = True  # setze Leuchtdiode in Zeile 2, Spalte 2

    elif (microbit.acc_x <= -0.25) and (microbit.acc_x > -0.5):  # (x <= -0.25) and (x > -0.5)
        microbit.leds[2][1] = True  # setze Leuchtdiode in Zeile 2, Spalte 3

    elif microbit.acc_x <= -0.5:  # x <= -0.5
        microbit.leds[2][0] = True  # setze Leuchtdiode in Zeile 2, Spalte 4

    sleep(0.25)  # warte

microbit.close()  # schliesse den Kommunikationskanal zum Microbit

print('Programmende')