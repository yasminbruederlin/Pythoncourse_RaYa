# TA2 Überholendes Auto

In dieser Teilaufgabe integrieren wir das überholende Auto.
Die Positionierung des zu überholenden Fahrzeuges wird über einen Zufallsgenerator bestimmt. 
Python bietet für die Generierung von Zufallszahlen das Modul `random` an. Dieses Modul
wird als erstes auf Zeile 2 importiert `from random import random`. Die Generierung einer Zufallszahl
zwischen -2 und 2 mit einer Schrittweite von 1 erfolgt mittels  `round(random() * 4) - 2`.  
- random() => Zufallszahl zwischen 0.0 und 1.0
- round(...) => Funktion zur Rundung einer Fliesskommazahl

Die nachfolgende Anleitung soll dir helfen, die Umsetzung schrittweise durchführen zu können:

1. Variablendefinion des entgegenkommenden Fahrzeuges:
    - `random_position = round(random() * 4) - 2  # Zufallszahl für die Bestimmung der Position (-2, -1, 0, 1 , 2)`
    - `car_position_x = random_position  # Position auf der x Achse des Autos. Mögliche Positionen (-2, -1, 0, 1 , 2)`
    - `car_x = car_position_x * car_width + car_x_centre  # Position in Pixel auf der x Achse`
    - `car_y = -car_heigth  # Position in Pixel auf der y Achse`
    - `car_velocity = 15  # Geschwindigkeit des zu überholenden Fahrzeuges`
     
2. Bestimmung der Koordinaten des überholenden Fahrzeuges:
    - Mit der Variablen `car_velocity` wird die y Position des zu überholenden Fahrzeuges in
      jedem Zyklus angepasst. Die Berechnung der neuen y Position erfolgt als einfache
      Addition der aktuellen Position + Geschwindigkeit `car_y += car_velocity`. 
      
    - In jedem Zyklus ist nach der Veränderung der y Position des zu überholenden Fahrzeuges zu 
      überprüfen, ob das Fahrzeug sich noch im sichtbaren Bereich des Displays befindet. Ist dies
      nicht der Fall, sind die x und y neu zu berechnen.  
       
      <img src="img/camtasia.gif" width="50%"><br>
      
    - Hinweis 1: Die Neuberechnung der y Position des zu überholenden Fahrzeuges bzw. der
      Variablen `random_position` führt in der Spiellogik zu einem Verhalten, welches nicht allzu
      herausfordernd für den Spieler ist. Dieser Effekt wird in der Teilaufgabe 3 optimiert.
      
    - Hinweis 2: Die Kollisionsdetektion erfolgt in der Teilaufgabe 5.
