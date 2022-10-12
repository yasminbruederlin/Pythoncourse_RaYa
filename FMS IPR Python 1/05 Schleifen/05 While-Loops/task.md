While-Loops
===========

In Python sind for-Loops nicht die einzige Art von Loops. Eine andere Art von Loops sind die **while-Loops**. While-Loops
sind im Gegensatz zu for-Loops unbestimmte Iterationen.

Ein while-Loop führt eine Reihe von Anweisungen aus, solange eine bestimmte Bedingung erfüllt ist.

Die Struktur folgt diesem Muster:

```python
while <Bedingung>:
  <Aktion>
```

Betrachten wir das folgende Beispiel, in dem wir die ganzen Zahlen 0 bis 3 ausgeben:

```python
count = 0
while count <= 3:
  # Schleifenkörper
  print(count)
  count += 1
```

Schauen wir uns das genauer an:

1. `count` wird anfangs auf 0 gesetzt. Die Bedingung im while-Loop lautet `count <= 3`. Bei der ersten Iteration der 
   Schleife ist die Bedingung also erfüllt. Also wird der Loop ausgeführt.

2. Innerhalb des Loops printen wir `count` und erhöhen den Wert anschliessend um 1.

3. Nach der ersten Iteration, kehrt Python an den Anfang des Loops zurück und überprüft die Bedingung erneut. 
   Nach der ersten Iteration wäre `count` also gleich 1. Somit wird die Bedingung immer noch als `True` ausgewertet und 
   der Loop erneut ausgeführt.

4. So geht es weiter, bis die Variable `count` den Wert 4 annimmt. Wenn die Bedingung geprüft wird, ist sie nun nicht mehr 
   wahr und der Loop wird beendet.
   
Es wird also folgendes geprinted:

```python
0
1
2
3
```

Einige Hinweise zu while-Loops:

**Einrückung:**

Ähnlich wie bei einem for-Loop wird alles, was auf der gleichen Einrückungsebene steht, bei jeder Iteration des Loops ausgeführt, 
solange die Bedingung erfüllt ist.

```python
count = 0
while count <= 3:
  # Schleifenkörper
  print(count)
  count += 1
  # Jeder andere Code auf dieser Einrückungsebene wird
  # bei jeder Iteration ausgeführt.
```

Wenn wir das Einrücken vergessen, erhalten wir einen `IndentationError`.

Aufgaben
--------

1. Untersuchen Sie den bereitgestellten while-Loop. Es gibt zusätzliche print()-Anweisungen, die helfen, die Iterationen 
   zu visualisieren. Führen Sie den Code aus, um zu sehen, was bei jeder Iteration der Schleife passiert. Wenn Sie fertig sind, 
   kommentieren Sie das Beispiel aus.

Da Sie nun auch Loops beherrschen hat die NASA angeklopft. Sie möchte ein Python-Programm, dass den Countdown für Ihre Raketen
herunterzählt.

Dafür brauchen Sie:

- Eine Variable, welche die Anzahl Iterationen zählt und  dazu beiträgt, dass unserer Loop schließlich stoppt.
- Eine Bedingung, die unseren while-Loop bei jeder Iteration prüft.
- Code-Anweisungen, die bei jeder Iteration des Loops ausgeführt werden.


2. Erstellen Sie eine Variable namens `countdown` und setzen Sie den Wert auf 10.

3. Definieren Sie einen while-Loop. Er soll ausgeführt werden, solange die Variable `countdown` größer oder gleich Null ist.

4. Bei jeder Iteration soll:

- der Wert von `countdown` geprinted werden.
- der Wert von `countdown` um 1 verringert werden.

5. Nach Beenden der Schleife soll das Progarmm noch "We have liftoff!" printen.
