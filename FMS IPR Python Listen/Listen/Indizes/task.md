Indizes
==========

Wir führen Vorstellungsgespräche mit Kandidaten für eine Stelle. Wir rufen jeden Bewerber der Reihe nach an, 
dargestellt durch die folgede Python-Liste:

```python
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
```

Zuerst rufen wir "Juan" an, dann "Zofia", etc.

In Python nennen wir die Position eines Elements in einer Liste seinen **Index**.

In Python besitzt das erste Element in einer Liste den Index 0 und nicht 1.

Hier sind die Indexnummern für die Listenaufrufe:

|Element| Index|
|-------|-----|
|"Juan" | 0
|"Zofia"| 1
|"Amare"| 2
|"Ezio" | 3
|"Ananya"| 4

In diesem Beispiel ist das Element mit dem Index 2 "Amare".

Wir können ein einzelnes Element aus einer Liste auswählen, indem wir eckige Klammern (`[]`) und den Index des Listenelements 
verwenden. 

```python
print(calls[2])
```

Printed also folgendes:

```python
Amare
```

Hinweis: Wenn Sie auf Elemente einer Liste zugreifen, müssen Sie einen int als Index verwenden. Wenn Sie einen Float verwenden, erhalten Sie einen Fehler. Dies kann besonders schwierig sein, wenn Sie Divisionen verwenden. Zum Beispiel wird `print(calls[4/2])` zu einem Fehler führen, weil `4/2` als Float `2.0` ausgewertet wird.

Um dieses Problem zu lösen, können Sie mit der Funktion `int()` erzwingen, dass das Ergebnis Ihrer Division ein int ist. `int()` nimmt eine Zahl und entfernt das Dezimalkomma und alles danach. Zum Beispiel werden `int(5.9)` und `int(5.0)` beide zu `5`. Also ergeben `calls[int(4/2)]` denselben Wert wie `calls[2]`, während `calls[4/2]` zu einem Fehler führt.

Aufgaben
-----------

1. Verwenden Sie eckige Klammern, um die 4. Person aus der Liste `employees` auszuwählen. Speichern Sie sie in der Variablen 
   `employee_four` und printen Sie den Wert der Variable.

2. Entfernen Sie das Kommentarzeichen. Was geschieht? Und warum?

3. Die Auswahl eines Elements, das nicht existiert, erzeugt einen `IndexError`. Ändern Sie den Index an auf die grösste Zahl, 
   sodass Sie keinen `IndexError` erhalten.


