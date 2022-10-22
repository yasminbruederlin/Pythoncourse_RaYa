Loops 2.0 - überflüssiger Abschnitt?
===========

Bevor wir unsere eigenen Loops erstellen, wollen wir die Motivation dahinter kennenlernen. Dafür betrachten wir ein Beispiel
bei welchem wir nicht die Hilfe von einem Loop verwenden.

Nehmen wir an, wir haben eine Liste von Zutaten und wollen jedes Element der Liste ausdrucken:

```python
ingredients = ["Milch", "Zucker", "Vanilleextrakt", "Teig", "Schokolade"]
```

Wenn wir nur print() verwenden, könnte unser Programm wie folgt aussehen:

```python
print(ingredients[0])
ausdrucken(ingredients[1])
ausdrucken(ingredients[2])
ausdrucken(ingredients[3])
print(ingredients[4])
```

Printed folgendes:

```python
Milch
Zucker
Vanilleextrakt
Teig
Schokolade
```

Dieses Beispiel ist noch überschaubar. Wir schreiben nur 5 print()-Anweisungen. 
Wenn wir uns aber nun vorstellen, dass die Liste 10 oder 24601 oder ... 100.000.000 Elemente besitzt. 
In diesem Fall würde es Ewigkeiten dauern, bis wir alle print Befehle geschrieben hätten. Zudem würden wir wahrscheinlich
noch etliche Fehler begehen, indem wir uns vertippen.

<span style="color:turquoise;font-weight:700;font-size:25px">
Aufgabe
</span>

Verwenden Sie den `print()` Befehl um 10-mal `"This can be so much easier with loops!"` zu printen.
