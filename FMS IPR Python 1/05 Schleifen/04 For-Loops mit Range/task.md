For-Loops mit Range
===================

Oft möchten wir gar nicht durch eine Liste iterieren, sondern nur eine bestimmte Aktion mehrmals ausführen.

Wenn wir z.B. mit einem for-Loop sechsmal die Meldung "Ich lerne gerade Loops!" ausgeben wollen, würden wir folgendermassen vorgehen:

```python
for <temporäre Variable> in <Liste der Länge 6>:
  print("Ich lerne gerade 01 Loops!")
```

Beachten Sie, dass wir eine Liste mit einer Länge von sechs durchlaufen müssen, aber es ist uns nicht unbedingt wichtig, 
was sich in der Liste befindet.

Damit wir immer eine Liste mit der richtigen Länge besitzen, können wir die Funktion `range()` verwenden.

Der folgende Code erzeugt eine Sammlung von 6 ganzzahligen Elementen von 0 bis 5:

```python
six_steps = range(6)
 
# six_steps ist nun eine Sammlung mit 6 Elementen:
# 0, 1, 2, 3, 4, 5
```

Wir können das range-Objekt direkt in unseren for-Loops als "Liste" verwenden, um eine Iteration sechsmal durchzuführen:

```python
for temp in range(6):
  print("Ich lerne gerade 01 Loops!")
```

Printed folgendes:

```python
Ich lerne gerade Loops!
Ich lerne gerade Loops!
Ich lerne gerade Loops!
Ich lerne gerade Loops!
Ich lerne gerade Loops!
Ich lerne gerade Loops!
```

Es ist zu beachten, dass wir die Variable `temp` nirgendwo innerhalb des Loops verwenden. 
Wenn wir wissen wollen, in welcher Iteration des Loops wir uns befinden, können wir `temp` verwenden, um dies zu verfolgen. 
Da unser range-Objekt bei 0 beginnt, fügen wir + 1 zu `temp` hinzu, um die Anzahl der Iterationen unserer Schleife genauer 
darzustellen.

```python
for temp in range(6):
  print("Wir befinden uns in der " + str(temp + 1) + ". Iteration.")
```

Printed folgendes:

```python
Wir befinden uns in der 1. Iteration.
Wir befinden uns in der 2. Iteration.
Wir befinden uns in der 3. Iteration.
Wir befinden uns in der 4. Iteration.
Wir befinden uns in der 5. Iteration.
Wir befinden uns in der 6. Iteration.
```

Aufgabe
---------
1. Verwenden Sie `range()` um den Wert der Variable `promise`5-mal zu printen.

