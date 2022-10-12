Remove
=========

Mit `.remove()` (Listenmethode) können wir gezielt Elemente aus einer Liste entfernen.

Nehmen wir an, wir haben eine Liste namens `shopping_line`, die ein Regal in einem Lebensmittelgeschäft darstellt:

```python
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
```

Wir könnten `"Chris"` entfernen, indem wir die Methode `.remove()` verwenden:

```python
shopping_line.remove("Chris")
 
print(shopping_line)
```

Wir sehen, dass `"Chris"` nicht mehr enthalten ist:

Wir können `.remove()` auch auf eine Liste anwenden, die doppelte Elemente enthält.

Dabei wird nur das erste Vorkommen des passenden Elements entfernt:

```python
# Erstellen Sie eine Liste
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Ein Element entfernen
shopping_line.remove("Chris")
print(einkauf_zeile)
```

Printed folgendes:

```python
["Cole", "Kip", "Sylvana", "Chris"]
```

Aufgaben
---------

Wir haben beschlossen, in das Lebensmittelgeschäft einzusteigen. Unsere Managerin Calla hat beschlossen, alle Inventareinkäufe 
in einer Liste zu speichern, damit wir wissen, welche Produkte bestellt werden müssen.

1. Erstellen Sie eine Liste namens `order_list` mit den folgenden Werten (in dieser Reihenfolge):
"Sellerie", "Orangensaft", "Orange", "Fladenbrot".
 
Wir haben Glück! Wir haben tatsächlich eine Kiste "Fladenbrot" in unserem Lager gefunden. Wir brauchen es nicht mehr zu 
bestellen.  

2. Entfernen wir es aus `order_list` mit der Methode `.remove()`. Printen Sie die Liste.

Unser Geschäft ist zu einem großen Erfolg geworden! Wir haben beschlossen, einen zweiten Laden zu eröffnen und benötigen eine neue Bestellliste. Calla hat uns den Gefallen getan, eine solche zusammenzustellen.

3. Erstellen Sie eine neue Liste mit dem Namen `new_store_order_list` und weisen Sie ihr die folgenden Werte zu (in der Reihenfolge):
"Orange", "Apfel", "Mango", "Brokkoli", "Mango"

Hinweis: Unsere zweite Filiale wird zwei Bestellungen von Mangos benötigen, daher wird der Wert dupliziert.

Wir haben wieder Glück! Wir haben tatsächlich eine Kiste "Mango" in unserem Lager gefunden.
Wir werden nicht mehr zwei Bestellungen aufgeben müssen.

4. Entfernen Sie eine Mange aus `new_store_order_list` und printen Sie die Liste.
