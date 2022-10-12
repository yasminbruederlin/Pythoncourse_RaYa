# Listen
Listen erweitern die Funktionalität von Tuples. Im Gegensatz zu den Tuples, sind Listen zur
Laufzeit von Python veränderbar.  

## Erstellung
Listen können auf zwei Arten erstellt werden:
- Fix hinterlegt im Quellcode, also gleich wie Tuples
- Zur Laufzeit

Im Gegensatz zu den Tuples sind die Liestenelement in eckigen Klammern `[]` einzufassen. 

```python
colors = ['rot', 'blau', 'grün']
```

## Laufzeitoperationen
Neue Elemente werden zur Laufzeit mittels `append()` hinzugefügt.
```python
colors.append('weiss')
```

Mehrere Elemente durch Addition.
```python
colors = colors + ['weiss', 'türkis', 'violett']
```

Das entfernen erfolgt mittels `pop()`.
```python
colors.pop()  # Entfernung des letzten Elementes
colors.pop(0)  # Entfernung des Elementes mit dem Index 0
```

Ähnlich wie bei den Strings lassen sich Bereiche von Listen über das Slicing abfragen.
```python
colors[0]  # erstes Element
colors[-1]  # letztes Element
colors[:3]  # die ersten drei Elemente
colors[-3:]  # die letzten drei Elemente
colors[-3:]  # die letzten drei Elemente
colors[1:4]  # das 1. bis zum 3. Element
```

Bestehende Elemente können überschrieben werden.
```python
colors[1] = 'schwarz'
```
