Indizes 2.0
=============

Wir können den Index `-1` verwenden, um das letzte Element einer Liste auszuwählen. Dafür müssen wir auch nicht wissen, wie viele 
Elemente in einer Liste enthalten sind.

```python
pancake_recipe = ["Eier", "Mehl", "Butter", "Milch", "Zucker", "Liebe"]
```

Wenn wir den Index `-1` wählen, erhalten wir das letzte Element, `"Liebe"`.

```python
print(pfannkuchen_rezept[-1])
```

Printed also folgendes:

```python
Liebe
```

Dies ist gleichbedeutend mit der Auswahl des Elements mit dem Index 5:

```python
print(pfannkuchen_rezept[5])
```

Printed ebenfalls:

```python
Liebe
```

Hier sind die negativen Indexzahlen für unsere Liste:

|Element | Index|
|--------|------|
|"Eier"| -6
|"Mehl"| -5
|"Butter"| -4
|"Milch"| -3
|"Zucker"| -2
|"Liebe"| -1

Aufgabe
---------

1. Erstellen Sie eine Variable `last_element` und verwenden Sie den Index `-1` um Ihr das letzte Element der Liste zuzuweisen.
Printen Sie anschliessend `last_element`.
