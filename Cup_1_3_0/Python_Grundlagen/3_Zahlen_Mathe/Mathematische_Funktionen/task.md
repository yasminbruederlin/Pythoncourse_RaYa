# Mathematische Funktionen

Python bietet eine Vielzahl eingebauter mathematischer Funktionen für die Verarbeitung von Zahlenwerten  
(https://docs.python.org/3/library/functions.html).  

Exemplarische betrachten wir die drei, vermutlich am häufigsten gebrauchten, Funktionen:

## `round()`: Rundung von Zahlen
Die Rundungsfunktion erlaubt eine unterschiedliche Nutzung:
- Aufruf der Funktion ohne zweiten Parameter in der Klammer => Rundung einer Zahl zum nächsten Integerwert.
- Aufruf der Funktion mit Angabe eines zweiten Parameters für die Anzahl Nachkommastellen.

## `abs()`: Bestimmung des Absolutwertes einer Zahl
Berechnung des Absolutwertes einer Zahl.
$|-1.369| = 1.369$    

## `pow()`: Potenzfunktion
Für die Berechung von Potenzen steht nebst dem Doppelsteroperator `**` auch noch die `pow()` Funktion
zur Verfügung.  
$3^2$ in Python `3.0**2.0` oder `pow(3.0, 2.0)`