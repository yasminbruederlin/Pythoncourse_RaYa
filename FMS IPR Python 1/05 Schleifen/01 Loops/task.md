Loops
======


In unserem Alltag neigen wir dazu, viele Prozesse zu wiederholen, ohne es zu merken.

Wenn wir zum Beispiel ein leckeres Rezept kochen wollen, müssen wir unsere Zutaten vorbereiten, indem wir sie zerkleinern. 
Wir hacken und hacken und hacken, bis alle unsere Zutaten die richtige Größe haben. An diesem Punkt hören wir auf zu hacken.

Wenn wir unsere Zerkleinerungsaufgabe in eine Reihe von drei kleineren Schritten aufteilen, haben wir:

1. Eine <span style="color:yellow;font-weight:100;font-size:15px">
Initialisierung</span>: Wir sind bereit zu kochen und haben eine Sammlung von Zutaten, die wir zerkleinern wollen.
2. Eine <span style="color:orange;font-weight:100;font-size:15px">
Wiederholung</span>: Wir beginnen mit der ersten Zutat und hacken los. Wir führen die Aktion des Zerkleinerns immer wieder für jede unserer Zutaten aus.
3. Eine <span style="color:red;font-weight:100;font-size:15px">
Endbedingung</span>: Wir sehen, dass wir keine Zutaten mehr zu hacken haben und hören auf.

~~Beim Programmieren wird dieser Prozess der eine Initialisierung, Wiederholungen und eine Endbedingung beinhaltet, **Loop** 
genannt.~~ In einem *Loop* bzw. einer *Schleife* führen wir Aufgaben aus, welche sich wiederholen. ~~Diesen Prozess~~ Eine Wiederholung nennen wir *Iteration*.

***TODO: braucht es diesen folgenden Abschnitt? evtl weglassen***
```
In Python gibt es zwei Arten von Iterationen:

1. **Unbestimmte Iteration**, bei der die Anzahl der Schleifenausführungen davon abhängt, wie oft eine Bedingung erfüllt ist.
2. **Bestimmte Iteration**, bei der die Anzahl der Schleifenausführungen im Voraus festgelegt wird.

Typischerweise werden Loops verwendet, um über eine Sammlung von Elementen zu iterieren. Im obigen Beispiel können wir 
uns die Zutaten, die wir zerkleinern wollen, als unsere Sammlung vorstellen. Dies ist eine Form der bestimmten ~~definitiven~~ Iteration, 
da wir im Voraus wissen, wie lang unsere Sammlung ist und somit wissen, wie oft wir die Sammlung der Zutaten durchlaufen müssen.

Einige Sammlungen können klein sein - wie eine kurze Zeichenkette -, während andere Sammlungen riesig sein können - wie 
ein Zahlenbereich von 1 bis 10.000.000! Aber keine Sorge, Loops bieten uns die Möglichkeit, mit beide Sorten einfach umzugehen. 
Dieses einfache, aber leistungsfähige Konzept spart uns viel Zeit und erleichtert uns die Arbeit mit großen Datenmengen.

In dieser Lektion lernen wir, wie wir mit Python sowohl bestimmte als auch unbestimmte Iterationen in unseren eigenen Programmen implementieren können.
```

<span style="color:turquoise;font-weight:700;font-size:25px">
Aufgabe
</span>


Hacken Sie alle Zutaten der Zutatenliste im Pythonprogramm. Sie können dazu mit Indexierung auf die einzelnen Elemente der Liste zugreiffen und diese mit `print( ... + " hacken")` ausgeben. 
