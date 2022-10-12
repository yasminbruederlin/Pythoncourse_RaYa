Funktionsaufruf
======

Nachdem wir nun geübt haben, eine Funktion zu definieren, wollen wir nun lernen, wie man eine Funktion aufruft, um den Code im _function body_ auszuführen.

Das Ausführen dieses Codes wird Funktionsaufruf genannt. Um eine Funktion in Python aufzurufen, geben Sie den Funktionsnamen gefolgt von Klammern `( )` ein.

Schauen wir uns unsere Funktion `directions_to_timesSq()` noch einmal an:

```python
def directions_to_timesSq():
  print("Laufen Sie 4 Minuten, um zur 34th St Herald Square Bahnstation zu gelangen.")
  print("Nehmen Sie den Zug N, Q, R oder W Richtung Norden, 1 Haltestelle.")
  print("Steigen Sie an der Haltestelle Times Square 42nd Street aus.")
```

Um unsere Funktion aufzurufen, müssen wir den Namen der Funktion gefolgt von einem Klammerpaar eingeben:

```python
directions_to_timesSq()
```

Der Aufruf der Funktion führt die prints innerhalb des Textkörpers aus. Wir erhalten:

```python
Laufen Sie 4 Minuten, um zur 34th St Herald Square Bahnstation zu gelangen.
Nehmen Sie den Zug N, Q, R oder W in Richtung Norden, 1 Haltestelle.
Steigen Sie an der Haltestelle Times Square 42nd Street aus.
```

Beachten Sie, dass Sie eine Funktion erst aufrufen können, nachdem sie in Ihrem Code definiert wurde.


Aufgaben
----------

1. Kopieren und fügen Sie den Code aus der letzten Übung ein.

2. Rufen Sie die Funktion `directions_to_timesSq()` auf.
