Verschachtelte Schleifen
=========================

Loops können auch verschachtelt werden. 

Nehmen wir an, wir sind für eine Klasse verantwortlich, die in drei Projektteams aufgeteilt ist:

```python
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
```

Die Verwendung eines for- oder while-Loops kann hier nützlich sein, um jedes Team zu erhalten:

```python
for team in projekt_teams:
  print(team)
```

Printed folgendes:

```python
["Ava", "Samantha", "James"]
["Lucille", "Zed"]
["Edgar", "Gabriel"]
```
Was aber, wenn wir jeden einzelnen Schüler printen wollen? In diesem Fall müssten wir unsere Loops verschachteln, 
um jede Teilliste durchlaufen zu können. Das würde folgendermassen aussehen:

```python
# iteriere durch jede Teilliste
for team in project_teams:
  # iteriere über die Elemente in jeder Teilliste
  for student in team:
    print(student)
```

Printed folgendes:

```python
Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel
```

Aufgaben:

Fred & George's Geschäft mit den magischen Süssigkeiten läuft wie verrückt. Mittlerweile haben Sie bereits 3 verschiedene
Läden eröffnet. Leider haben Sie nun die Übersicht über Ihre Verkäufe verloren und brauchen deshalb wieder Ihre Hilfe!

Fred & George haben Ihnen die Liste `sales_data` zur Verfügung gestellt, die die Anzahl der verschiedenen verkauften Süssigkeiten an den drei verschiedenen
Standorten zeigt.

Ihr Auftrag lautet die Gesamtzahl der verkauften Süssigkeiten zusammen zu zählen. 

1. Definieren Sie zunächst eine Variable `sweets_sold` und setzen Sie sie auf Null.
   
2. Iterieren Sie über die Liste `sales_data`, indem Sie die folgenden Richtlinien befolgen:

- Nennen Sie die temporäre Variable des for-Loops `location`.
- printen Sie jede Standortliste.

3. Erstellen Sie innerhalb unseres Loops für `sales_data` einen zweiten Loop, um über jedes Element der Unterliste `location` 
   zu iterieren. Addieren Sie den Wert des Elementes jeweils zu `sweets_sold`. Somit sollten Sie am Ende die Summe aller Zahlen
   aus der verschachtelten Liste `sales_data` haben.

4. Geben Sie den Wert von `sweets_sold` außerhalb der verschachtelten Schleife aus.
