# Zahlenvariablen
Variablen, denen numerische Werte zugewiesen sind, können genauso behandelt werden wie die Zahlen selbst. ~~Zwei Variablen können addiert, durch 2 geteilt und mit einer dritten Variable multipliziert werden, ohne dass Python zwischen den Variablen und den Literalen (wie der Zahl 2 in diesem Beispiel) unterscheidet.~~ Wenn Sie mit Variablen rechnen, wird die Variable nicht verändert - Sie können eine Variable nur mit dem Zeichen = verändern ~~aktualisieren~~.

```python
# Erstellen zweier Zahlenvariablen 
nr_people = 100
price_entry = 15

# Ausgabe der Variablenwerte
print(nr_people)
print(price_entry)
# printed 100 und 15

# Multiplikation zweier Zahlenvariablen
print(nr_people * price_entry)
# printed 1'500

# Preiserhöhung $$$ - zu gewagt? 
price_entry = price_entry + 5

# Multiplikation zweier Zahlenvariablen
print(nr_people * price_entry)
# printed ?

```

~~Im oberen Beispiel wurden zwei Variablen erstellt, die Zahlen speichern. Wenn wir eine Berechnung durchführen, werden
 die Variablen nicht aktualisiert! Wenn wir die Variable `price_entry` verändern und die Berechnungen
 erneut durchführen, werden die aktualisierten Werte für die Variablen verwendet!~~

## Aufgabe
Erstellen Sie die Variablen `price_pizza` und `nr_orders`. Printen Sie die Kosten, wenn eine
Pizza 18 CHF kostet und Sie 7 Bestellungen haben.
