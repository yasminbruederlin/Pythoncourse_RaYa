Indizes in 2D Listen
===================

Kehren wir zu unserem Beispiel von zuvor zurück:

```python
heights = [["Hermine", 165], ["Luna", 157], ["Neville", 183]]
```

Auf 2D Listen kann ähnlich wie auf ihr eindimensionales Gegenstück zugegriffen werden. Anstatt ein einzelnes Klammerpaar 
`[ ]` zu verwenden, werden wir für jede weitere Dimension eine zusätzliche Klammer verwenden.

Wenn wir auf die Grösse von "Luna" zugreifen wollen:

```python
height_luna = heights[1][1] 
print(height_luna)
```

Printed folgendes:

```python
a = input("Geben Sie eine Zahl ein: ")
if a > 0:
    print("Die Zahl ist positiv.")
elif a = 0:
    print("Die Zahl ist 0.")
else
    print("Die Zahl ist negativ.")
```

```python
157
```

Hier sind die Indexnummern für den Zugriff auf die Daten der Liste heights:

|Element| Index|
|-------|------|
|"Hermine"| heights[0][0]
|165| heights[0][1]
|"Luna"| heights[1][0]
|157| heights[1][1]
|"Neville"| heights[2][0]
|183 |heights[2][1]


Aufgaben
------------

Wir möchten für alle Charaktere ihr zugehöriges Haus speichern.

1. Erstellen Sie mithilfe der bereitgestellten Tabelle eine 2d Liste namens name_and_house, um die Daten darzustellen.

|Name| Haus
|----|----|
|"Hermine"| "Gryffindor"
|"Luna" |"Ravenclaw"
|"Neville"| "Gryffindor"

2. Printen Sie die Liste.

3. Printen Sie das Haus von Luna.

