# Zahlenvariablen


Variablen, denen numerische Werte zugewiesen sind, können genauso behandelt werden wie die Zahlen selbst. Zwei Variablen können addiert, durch 2 geteilt und mit einer dritten Variable multipliziert werden, ohne dass Python zwischen den Variablen und den Literalen (wie der Zahl 2 in diesem Beispiel) unterscheidet. Wenn Sie mit Variablen rechnen, wird die Variable nicht verändert - Sie können eine Variable nur mit dem Zeichen = aktualisieren.

```python
nr_people = 100
price_entry = 15

# printed 1'500
print(nr_people * price_entry)

# printed 100 und 15
print(nr_people)
print(price_entry)

# Preiserhöhung $$$
price_entry = 20

# printed ?
print(nr_people * price_entry)

# printed 100 und 20
print(nr_people)
print(price_entry)
```

  

Im oberen Beispiel wurden zwei Variablen erstellt, die Zahlen speichern. Wenn wir eine Berechnung durchführen, werden
 die Variablen nicht aktualisiert! Wenn wir die Variable `price_entry` verändern und die Berechnungen
 erneut durchführen, werden die aktualisierten Werte für die Variablen verwendet!



## Aufgabe


Erstellen Sie die Variablen `price_pizza` und `nr_orders`. Printen Sie die Kosten, wenn eine
Pizza 18 CHF kostet und Sie 7 Bestellungen haben.