Zusammenfügen von Listen
==========================
Um mehrere Listen zusammenzufügen können wir `+` verwenden. 

Im folgenden Beispiel betrachten wir die verkauften Produkte einer Bäckerei.

```python
items_sold = ["Kuchen", "Kekse", "Brot"]
```

Angenommen, die Bäckerei möchte nun auch noch `"Pralinen"` und `"Torten"` verkaufen:

```python
items_sold_new = items_sold + ["Keks", "Torte"]
print(artikel_verkauft_neu)
```

Printed folgendes:

```python
['Kuchen', 'Keks', 'Brot', 'Keks', 'Torte']
```

In diesem Beispiel haben wir eine neue Variable, `items_sold_new`, erstellt. Sie enthält sowohl die ursprünglich verkauften 
als auch die neuen Artikel enthält. Wir können die ursprüngliche Variable `items_sold` überprüfen und sehen, dass sie 
sich nicht geändert hat:

```python
print(items_sold)
```
Printed folgendes:

```python
['Kuchen', 'Keks', 'Brot']
```

Achtung: Wir können `+` nur mit anderen Listen verwenden. Wenn wir diesen Code eintippen:

```python
list = [1, 2, 3]
list + 4
```

erhalten wir nämlich die folgende Fehlermeldung:

```python
TypeError: can only concatenate list (not "int") to list
```

Wenn wir ein einzelnes Element mit `+` hinzufügen wollen, müssen wir es in eine Liste mit Klammern (`[]`) einfügen:

```python
my_list + [4]
```

Aufgaben
-------

Krillin überarbeitet gerade seine Liste `orders`, da er eine neue Bestellung für `"Veilchen"` und `"Edelweisse"`
erhalten hat.

1. Erstellen Sie eine neue Liste `new_orders` in der Sie die neuen Bestellungen speichern.

2. Erstellen Sie eine neue Liste `all_orders`. Verwenden Sie `+` um Ihr die Werte von `order` und `new_orders` zuzuweisen.

3. Printen Sie alle Bestellungen.

4. Finden und beheben Sie den Fehler von `broken_list`.
