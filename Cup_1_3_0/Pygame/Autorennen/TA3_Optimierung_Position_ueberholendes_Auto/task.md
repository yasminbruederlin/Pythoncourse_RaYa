# TA3 Optimierung Position überholendes Auto

Die Teilaufgabe 3 optimiert die Postionierung des zu überholenden Fahrzeuges.

Die nachfolgende Anleitung soll dir helfen, die Umsetzung schrittweise durchführen zu können:

1.  Definition einer neuen Variable  
    `random_position_old = random_position  # Hilfsvariable zur Optimierung der Postionierung`  
    Mithilfe der Variablen `random_position_old` wird die Positionierung des zu überholenden Fahrzeuges
    optimiert. 

2.  Optimierung der neuen Position des zu überholenden Fahrzeuges in Abhängigkeit des eigenen Fahrzeuges.
    
    ````python
    # Falls das zu überholende Fahrzeug am unteren Bildrand angelangt ist, wird die x Position
    # und die y Position neu bestimmt => nächstes zu überholendes Fahrzeug
    if car_y > canvas_height:
        while random_position == random_position_old:  # solange die neue Position der alten entspricht
            random_position_temp = round(random() * 2)  # temporäre Variable
            if my_car_position_x == -2:  # Position -2 => linker Rand
                random_position = -2 + random_position_temp  # Berechnung der neuen Position
            elif (my_car_position_x >= -1) and (my_car_position_x <= 1):  # Position -1, 0, 1
                random_position = my_car_position_x + random_position_temp - 1  # Berechnung der neuen Position
            elif my_car_position_x == 2:  # Position 2 => rechter Rand
                random_position = 2 - random_position_temp  # Berechnung der neuen Position
        # Die neue und die alte Position werden gleichgesetzt. 
        # Im nächsten Iterationszyklus erfolgt die Auswertung
        random_position_old = random_position 
    ````
       
    <img src="img/camtasia.gif" width="50%"><br>
    
    Hinweis: Da dieser Algorithmus etwas schwieriger in der Umsetzung ist, besteht diese Teilaufgabe primär in der
    Analyse und Übertragung des obigen Codefragmentes in die Pythondatei `car_race_3.py`.
      
