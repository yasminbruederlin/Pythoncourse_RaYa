# Die for Schleife

Eine `for` Schlaufe wiederholt einen Codeblock solange der zu Beginn definierte Bereich nicht vollständig
durchlaufen worden ist.

## Die range Funktion
Mit der `range` Funktion werden Bereiche definiert (siehe auch das folgende Kapitel). Diese
Bereichsdefinition legt die Anzahl der Durchläufe einer `for` Schlaufe fest.

```python
range(start, end, increment)
```
Die drei Elemente bedeuten:
- **start**: Startwert des Bereiches
- **end**: Endwert des Bereiches (Hinweis: Bei der Iteration wird der Endwert um die Zahl 1 versetzt nicht erreicht!)
- **increment**: Schrittweite

## Anwendung der for Schleife
Die Umsetzung einer `for` Schleife in Python erfolgt ähnlich zur `while` Schleife mittels
1. Das `for` Schlüsselwort gefolgt von einer Laufvariablen.
2. Das `in` Schlüsselwort welches den Bezug zum durchlaufenden Bereich erstellt.
3. Der zu durchlaufenden Bereiche. Der Begriff Bereich kann in Python sehr allgemein
betrachtet werden. In diesem Buch beschränken wir uns aber auf Zahlenbereiche.
   
```python
for i in range(0, 4, 1):
    print(i)
```
