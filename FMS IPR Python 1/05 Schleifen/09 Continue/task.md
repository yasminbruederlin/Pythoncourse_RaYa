Continue
=========

Die break-Anweisung von zuvor ist sehr nützlich. Es gibt aber auch Situationen, in denen wir den Loop nicht ganz beenden wollen. 
Was ist, wenn wir beispielsweise nur die aktuelle Iteration des Loops überspringen wollen?

Nehmen wir diese Liste von Zahlen als Beispiel:

```python
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
```

Was, wenn wir alle Zahlen in einer Liste ausgeben wollen, aber nur, wenn es sich um positive Zahlen handelt? 
In diesem Fall können wir die continue-Anweisung verwenden.

```python
for i in big_number_list:
  if i <= 0:
    continue
  print(i)
```

Dies printed folgendes:

```python
1
2
4
5
2
```

Erklärung: Ähnlich wie bei der break-Anweisung ist die continue-Anweisung in der Regel mit einer Form von Bedingung (if/elif/else) verbunden.
Sobald unser Loop das erste Mal auf ein Element (-1) stösst, wird die continue-Anweisung ausgeführt. Somit wird die aktuelle Iteration übersprungen 
und der Loop geht zum nächsten Element in der Liste über (4).
Bei der Ausgabe werden also positive Zahlen geprinted, da unsere Schleife das printen der negativen Zahlen jeweils überspringt.

Aufgabe
--------

Ihr Computer ist neuerding der Türsteher einer Bar, in der das Mindestalter 18 Jahre beträgt.

1. Gehen Sie die Altersliste durch. Überspringen Sie alle Einträge die kleiner als 18 sind und fahren Sie mit dem nächsten Eintrag fort. 
   Ansonsten printen Sie das Alter.
