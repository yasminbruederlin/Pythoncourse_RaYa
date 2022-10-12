Append
===========
Mit `.append()` können wir ein einzelnes Element zu einer Liste hinzufügen.

Nehmen wir an, wir haben eine leere Liste namens garden:

```python
garden = []
```

Mit `.append()` können wir das Element "Tomaten" hinzufügen:

```python
garden.append("Tomaten")
 
print(garten)
```

Printed folgendes:

```python
['Tomatoes']
```

Wenn wir `.append()` auf eine Liste anwenden, die bereits Elemente enthält, wird unser neues Element an das Ende der Liste angefügt:

```python
# Erstellen einer Liste
garden = ["Tomaten", "Weintrauben", "Blumenkohl"]
 
# Anhängen eines neuen Elements
garden.append("Grüne Bohnen")
print(garden)
```

Printed folgendes:
```python
['Tomaten', 'Weintrauben', 'Blumenkohl', 'Grüne Bohnen']
```

Aufgaben
------------

Krillin arbeitet in einem Gartenfachgeschäft namens Petal Power. Krillin hält die Bestellungen in einer Liste namens 
   `orders` fest.

1. Verwenden Sie `print`, um die Bestellungen zu prüfen, die er heute erhalten hat.

2. Krillin hat gerade eine neue Bestellung für "Tulpen" erhalten. Verwenden Sie `append`, um die Bestellungen hinzuzufügen.

3. Eine weitere Bestellung ist eingetroffen! Benutze `append`, um "Rosen" zu Bestellungen hinzuzufügen.

4. Printen Sie alle Bestellungen.

