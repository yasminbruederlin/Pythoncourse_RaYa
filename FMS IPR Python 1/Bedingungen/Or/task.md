Boolesche Operatoren: Or
==============

`or` ist ein weiterer **boolescher Operator**. Er kombiniert zwei Ausdrücke zu einem größeren Ausdruck, der wahr ist, 
wenn eine der Komponenten wahr ist.

> Orangen sind Früchte oder Äpfel sind ein Gemüse.

Diese Aussage besteht aus zwei Ausdrücken: `Orangen sind Früchte`, was Wahr ist, und `Äpfel sind ein Gemüse`, was Falsch ist. 
Da die beiden Ausdrücke durch `or` verbunden sind, ist die gesamte Aussage wahr. 

In der deutschen Sprache impliziert ein oder, dass wenn eine Komponente wahr ist, die andere Komponente falsch sein muss. 
Das ist in Python nicht der Fall. Wenn eine `or`-Anweisung aus zwei `True`-Komponenten hat, ist sie auch `True`.

```python
True or (3 + 4 == 7) # True
(1 - 1 == 0) or False # True
(2 < 0) or True # True
(3 == 8) or (3 > 4) # False
```

Aufgabe
------

1. Die FMS hat die Abschlussbedingungen milder gestaltet. Nun reicht es aus, nur eine der beiden Bedingungen
zu erfüllen. Schreiben Sie ein passendes if-statement dazu. Falls es wahr ist printen Sie:
   
> "Bravo! Sie erfüllen mindestens eine Bedingung."
