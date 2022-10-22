For-Loops
========
Der erste Loop-Typ den wir uns ansehen ist die **for-Loop**.

Bei einer For-Schleife wissen wir im Voraus, wie oft die Schleife iteriert werden muss. 
~~Ein for-Loop ist also eine bestimmte
Iteration.~~ In unseren Beispielen verwenden wir ~~Python-~~Listen als Sammlung von Elementen. 
Die For-Schleife lassen wir über alle Elemente der Liste laufen.

~~Mit for-Loops können wir bei jeder Iteration eine Aktion für jedes Element der Liste durchführen.~~

Bevor wir mit einer Liste arbeiten, wollen wir uns die allgemeine Struktur eines for-Loops ansehen:

```python
for <Element> in <Liste>:
  <Code>
```
Schauen wir uns das genauer an:

1. Das `for`-Keyword zeigt den Beginn eines for-Loops an.
2. `<Element>` wird verwendet, um das aktuelle Element der Liste in einer temporären Variable zu speichern. ~~in der Liste darzustellen.~~
3. Das `in`-Keyword trennt die temporäre Variable von der für die Iteration verwendeten Liste.
4. Die `<Liste>` ist eine ganz normale Python-Liste.
5. Der `<Code>` wird bei jeder Iteration des Loops ausgeführt.

Damit wir das Ganze etwas besser verstehen, verknüpfen wir diese Konzepte mit dem Zutaten-Beispiel. 
Lesen Sie das nebenstehende Programm (main.py) und führen Sie es aus. Was wird Ihnen im Terminal ausgeben?
Dieser for-Loop gibt jede Zutat in `ingredients` aus. 

In diesem Beispiel gilt:

1. `ingredient` ist das aktuelle `<Element>` der Liste bzw. die  `<temporäre Variable>`.
2. `ingredients` ist unsere `<Liste>`.
3. `print(ingredient)` ist der `<Code>`, die bei jeder Iteration ausgeführt wurde.
