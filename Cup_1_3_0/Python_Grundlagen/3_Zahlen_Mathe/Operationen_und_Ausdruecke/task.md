# Ganze und Fliesskommazahlen

Viele Rechenoperationen werden mit den vier Grundoperatoren `+ - * /` beschrieben. 
Im linken Programmierfeld findest du einige Beispiele.

**Wichtig**: Bei der Notation der Ausdrücke ist darauf zu achten, dass Zahlen ohne Kommas standardmässig
als Integer deklariert werden. Als Faustregel solltest du dir merken, dass bei der Zahlennotation 
die Kommannotation zu bevorzugen ist. 

## Modulo Operator
Der Modulooperator liefert den Rest einer Division als Resultat.

## Exponentialoperator
Der Exponentialoperator in Python wird durch doppelte `**` ausgedrückt.  
Beispiel: $3^2$ in Python `3**2`

## Rangfolge arithmetischer Ausdrücke
Bei der Verkettung von Ausdrücken gelten die Gesetmässigkeiten aus der Mathematik: "Punkt vor Strich"!
Python stellt somit eine einfach und intuitive Schnittstelle zur Verarbeitung von arithmetischen Ausrücken dar.
Die Verarbeitungsreihenfolge wird somit, wie in der Mathemaitk, durch die Operatoren und die Verwendung von
Klammertermen definiert.

Nachfolgend eine Uebersicht hinsichtlich der Dominanz in der Abarbeitung der einzelnen Operatoren:
1. `*`, `/`, `//` und `%` stehen auf gleicher Prioritätstufe
2. `+` und `-`sind den Punktoperatoren untergeordnet

