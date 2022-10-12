While-Loops mit Listen
======================

Genau wie for-Loops können wir auch mit while-Loops über Listen iterieren.

Dafür schauen wir uns unser Zutaten-Beispiel von zuvor an.

```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
```

Wir wissen, dass while-Loops eine Variable benötigen, um die Bedingung für den Start und das Ende des Loops festzulegen.

Was würden Sie in diesem Fall verwenden, um über die Liste `ingredients` zu iterieren und jedes Element zu printen.
Klicken Sie auf hint um die Lösung zu sehen.

<div class="hint">

Wir wissen, dass eine Liste eine bestimmte Länge hat. Wenn wir die Länge der Liste als Grundlage dafür verwenden, wie lange unsere while-Schleife laufen muss, können wir die genaue Länge der Liste iterieren. 
Dazu können wir die Funktion `len()` verwenden:

```python
# length ist in diesem Fall 5
length = len(ingredients)
```

</div>


Diese Länge können wir dann zusammen mit einer anderen Variable verwenden, um die Bedingung des while-Loops zu erstellen:

```python
length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1
```

Schauen wir uns das mal genauer an:

```python
# length ist in diesem Fall 5
length = len(ingredients)
```

Damit wir genügend oft (aber auch nicht zu oft) iterieren, müssen wir wissen, wie lang unsere Liste ist.
Aus diesem Grund speichern wir in der Variablen `length` die Länge der Liste.

```python
# Index beginnt bei Null
index = 0
```

Wir benötigen eine zusätzliche Variable, die wir mit unserer Länge vergleichen können. Aus diesem Grund definieren wir die Variable `index`.

```python
while index < length:
```

Für die Bedingung des while-Loops vergleichen wir nun die beiden erstellten Variablen.  

Bei der ersten Iteration lautet die Bedingung `0 < 5`. Dies wird als `True` ausgewertet und der Loop wird somit ausgeführt. 

```python
# Bei der ersten Iteration wird ingredients[0] geprinted.
print(ingredients[index])
```

Innerhalb des Loops können wir die Variable `index` verwenden, um auf unsere Liste `ingredients` zuzugreifen den entsprechenden
Wert in der Liste auszugeben.

Da unser Index bei Null beginnt, wird bei der ersten Iteration der Wert des Elements am nullten Index der Zutatenliste gedruckt. 
Bei der nächsten Iteration wird der Wert des Elements am ersten Index geprinted usw.

```python
# Index erhöhen, um auf das nächste Element in der Zutatenliste zuzugreifen.
# Jede Iteration führt dazu, dass die bald Bedingung nicht mehr erfüllt ist.
index += 1
```

Bei jeder Iteration unserer while-Schleife müssen wir auch den Wert von `index` erhöhen. Damit stellen wir sicher, 
dass unser Loop auch irgendwann beendet wird. 

Ausserdem bewirkt das Erhöhen auch, dass wir beim nächsten Durchlauf auf den nächsten Wert von `ingredients` zugreifen können.

Unsere endgültige Ausgabe würde lauten:

```python
milk
sugar
vanilla extract
dough
chocolate
```

Aufgaben
---------

Wir werden einen while-Loop erstellen, um über die bereitgestellte Liste `python_topics` zu iterieren.

Zunächst benötigen wir eine Variable, die die Länge der Liste angibt. Sie sagt uns, wie oft wir den Loop ausführen müssen.

1. Erstellen Sie eine Variable `length` und setzen Sie ihren Wert auf die Länge der Liste `python_topics`.

Als Nächstes benötigen wir eine Variable, die wir in der Bedingung mit unserer `length`-Variablen vergleichen können.

2. Erstellen Sie eine Variable namens `index` und initialisieren Sie den Wert auf 0.

3. Unsere Schleife soll über die Liste der `python_topics` iterieren und bei jeder Iteration `"I am learning about <Element aus python_topics>"` printen. 
