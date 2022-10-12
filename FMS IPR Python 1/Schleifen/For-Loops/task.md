For-Loops
========
Der erste Loop-Typ den wir uns ansehen ist die **for-Loop**.

Bei einem for-Loop wissen wir im Voraus, wie oft die Schleife iteriert werden muss. Ein for-Loop ist also eine bestimmte
Iteration. In unseren Beispielen verwenden wir Python-Listen als Sammlung von Elementen.

Mit for-Loops können wir bei jeder Iteration eine Aktion für jedes Element der Liste durchführen.

Bevor wir mit einer Liste arbeiten, wollen wir uns die allgemeine Struktur eines for-Loops ansehen:

```python
for <temporäre Variable> in <Liste>:
  <Code>
```

Schauen wir uns das genauer an:

1. Das `for`-Keyword zeigt den Beginn eines for-Loops an.
2. Die `<temporäre Variable>` wird verwendet, um den das aktuelle Element in der Liste darzustellen.
3. Das `in`-Keyword trennt die temporäre Variable von der für die Iteration verwendeten Liste.
4. Die `<Liste>` ist eine ganz normale Python-Liste.
5. Der `<Code>`, wird bei jeder Iteration des Loops ausgeführt.

Damit wir das Ganze etwas besser verstehen, verknüpfen wir diese Konzepte mit unserem Zutaten-Beispiel. 
Dieser for-Loop gibt jede Zutat in `ingredients` aus:

```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
for ingredient in ingredients:
  print(ingredient)
```

In diesem Beispiel gilt:

1. `ingredient` ist die `<temporäre Variable>`.
2. `ingredients` ist unsere `<Liste>`.
3. `print(ingredient)` war die `<Aktion>`, die bei jeder Iteration ausgeführt wurde.

Dieser Code printed also folgendes:

```python
milk
sugar
vanilla extract
dough
chocolate
```

Einige Hinweise zu for-Loops:

**Temporäre Variablen:**

Der Name einer temporären Variable ist frei wählbar und muss nicht vorher definiert werden. Die beiden folgenden 
Codeschnipsel tun genau das Gleiche wie unser obiges Beispiel:

```python
for i in ingredients:
  print(i)
for item in ingredients:
 print(item)
```

Da bei jeder Iteration unserer Schleife auf eine Zutat zugegriffen wird, ist es sinnvoller, unsere temporäre Variable 
`ingredient` zu nennen anstatt `i` oder `item`.

**Einrückung:**

Bei einem Loop muss die `<Aktion>` immer eingerückt sein. Alles, was auf eingerückt nach dem for-Loop steht, 
wird bei jeder Iteration der Schleife ausgeführt.

```python
for ingredient in ingredients:
  # Jeder Code auf dieser Ebene der Einrückung 
  # wird bei jeder Iteration der Schleife ausgeführt
  print(ingredient)
```

Falls wir das Einrücken vergessen, erhalten wir einen `IndentationError` oder ein unerwartetes Verhalten.

Aufgaben
---------

1. Führen Sie den Code aus. Es sollte ein IndentationError geben.

2. Korrigieren Sie den Code, indem Sie die richtige Zeile korrekt einrücken.

3. Schreiben Sie eine for-Loop, um alle Sportarten zu printen.
