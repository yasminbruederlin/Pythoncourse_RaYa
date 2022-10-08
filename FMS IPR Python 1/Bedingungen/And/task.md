Boolesche Operatoren: And
=========

Oft besteht eine Bedingung aus mehreren booleschen Ausdrücken. 
In diesen Fällen können wir größere boolesche Ausdrücke mit Hilfe von **booleschen Operatoren** bilden. Diese fassen 
kleinere boolesche Ausdrücke zu größeren booleschen Ausdrücken zusammen.

Es gibt drei boolesche Operatoren, die wir behandeln werden:

- `and`
- `or`
- `not`

`and` kombiniert zwei boolesche Ausdrücke und gibt `True` zurück, wenn beide Ausdrücke `True` sind. Sonst gibt es `False`zurück.

> Orangen sind eine Frucht und Karotten sind ein Gemüse.

Dieser boolesche Ausdruck besteht aus zwei kleineren Ausdrücken, nämlich `Orangen sind eine Frucht` und `Karotten sind ein Gemüse`
Da beide Ausdrücke wahr und durch den booleschen Operator `and` verbunden sind, ist der gesamte Ausdruck wahr.

Schauen wir uns ein Beispiel für einige AND-Anweisungen in Python an:

```python
(1 + 1 == 2) und (2 + 2 == 4) # True
 
(1 > 9) und (5 != 6) # False
 
(1 + 1 == 2) und (2 < 1) # False
 
(0 == 10) und (1 + 1 == 1) # False
```

Im zweiten und dritten Beispiel ist ein Teil des Ausdrucks wahr. Der gesamte Ausdruck ist aber 
falsch, weil die andere Aussage falsch ist. Die vierte Aussage ist ebenfalls falsch, da beide Komponenten falsch sind.

Aufgabe
--------

Kehren wir an die FMS zurück. Leider reicht es nicht, wenn man "nur" einen Notendurchschnitt von 4.0 besitzt.
Zusätzlich darf man auch nicht mehr als 20 unentschuldigte Versäumnisse besitzen.

1. Passen Sie das if-statement so an, dass es auch die Versäumnisse in Betracht zieht. Falls beide Bedingungen erfüllt sind, printen Sie

> "Bravo! Sie erfüllen alle Anforderungen."

